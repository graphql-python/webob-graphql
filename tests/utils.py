from webob import Request, Response


from webob_graphql import serve_graphql_request

import json

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


def url_string(**url_params):
    string = '/graphql'

    if url_params:
        string += '?' + urlencode(url_params)

    return string


def response_json(response):
    return json.loads(response.body.decode())


j = lambda **kwargs: json.dumps(kwargs)
jl = lambda **kwargs: json.dumps([kwargs])


class Client(object):
    def __init__(self, schema, settings):
        self.schema = schema
        self.settings = settings or {}

    def get(self, url, **extra):
        request = Request.blank(url, method='GET', **extra)
        context_value = self.settings.pop('context_value',request)
        response = serve_graphql_request(request, self.schema, context_value=context_value, **self.settings)
        return response

    def post(self, url, **extra):
        extra['POST'] = extra.pop('data')
        request = Request.blank(url, method='POST', **extra)
        context_value = self.settings.pop('context_value',request)
        response = serve_graphql_request(request, self.schema, context_value=context_value, **self.settings)
        return response

    def put(self, url, **extra):
        request = Request.blank(url, method='PUT', **extra)
        context_value = self.settings.pop('context_value',request)
        response = serve_graphql_request(request, self.schema, context_value=context_value, **self.settings)
        return response