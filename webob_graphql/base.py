from functools import partial

from webob import Response

from graphql_server import (HttpQueryError, default_format_error,
                            encode_execution_results, json_encode,
                            load_json_body, run_http_query)

from .render_graphiql import render_graphiql as default_render_graphiql


def serve_graphql_request(request, schema, pretty=None, response_class=None, graphiql_enabled=True,
                          batch_enabled=False, render_graphiql=None, format_error=None, encode=None, charset=None, **execute_options):
    if format_error is None:
        format_error = default_format_error

    if encode is None:
        encode = json_encode

    if response_class is None:
        response_class = Response

    if render_graphiql is None:
        render_graphiql = default_render_graphiql

    if charset is None:
        charset = 'UTF-8'

    try:
        request_method = request.method.lower()
        data = parse_body(request)

        show_graphiql = graphiql_enabled and request_method == 'get' and should_display_graphiql(request)
        catch = show_graphiql

        pretty = pretty or show_graphiql or request.params.get('pretty')

        execution_results, all_params = run_http_query(
            schema,
            request_method,
            data,
            query_data=request.params,
            batch_enabled=batch_enabled,
            catch=catch,

            # Execute options
            **execute_options
            # root_value=self.get_root_value(request),
            # context_value=self.get_context(request),
            # middleware=self.get_middleware(request),
            # executor=self.get_executor(request),
        )
        result, status_code = encode_execution_results(
            execution_results,
            is_batch=isinstance(data, list),
            format_error=format_error,
            encode=partial(encode, pretty=pretty)
        )

        if show_graphiql:
            return response_class(
                render_graphiql(
                    params=all_params[0],
                    result=result
                ),
                charset=charset,
                content_type='text/html'
            )

        return response_class(
            result,
            status=status_code,
            charset=charset,
            content_type='application/json'
        )

    except HttpQueryError as e:
        return response_class(
            encode({
                'errors': [format_error(e)]
            }),
            status=e.status_code,
            charset=charset,
            headers=e.headers or {},
            content_type='application/json'
        )


# noinspection PyBroadException
def parse_body(request):
    # We use mimetype here since we don't need the other
    # information provided by content_type
    content_type = request.content_type
    if content_type == 'application/graphql':
        return {'query': request.body.decode('utf8')}

    elif content_type == 'application/json':
        return load_json_body(request.body.decode('utf8'))

    elif content_type in ('application/x-www-form-urlencoded', 'multipart/form-data'):
        return request.params

    return {}


def should_display_graphiql(request):
    if 'raw' in request.params:
        return False

    return request_wants_html(request)


def request_wants_html(request):
    best = request.accept \
        .best_match(['application/json', 'text/html'])
    return best == 'text/html'
