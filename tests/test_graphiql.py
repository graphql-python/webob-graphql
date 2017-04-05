import pytest

from .schema import schema
from .utils import url_string, response_json, j, jl, Client

from webob_graphql.mako import render_graphiql as mako_render_graphiql


@pytest.fixture
def settings():
    return {}


@pytest.fixture
def client(settings):
    return Client(schema, settings)


@pytest.fixture
def pretty_response():
    return (
        '{\n'
        '  "data": {\n'
        '    "test": "Hello World"\n'
        '  }\n'
        '}'
    ).replace('\"','\\\"').replace('\n', '\\n')


def test_graphiql_is_enabled_by_default(client):
    response = client.get(url_string(), headers={'Accept': 'text/html'})
    assert response.status_code == 200
    assert response.content_type == 'text/html'


def test_graphiql_simple_renderer(client, pretty_response):
    response = client.get(url_string(query='{test}'), headers={'Accept': 'text/html'})
    assert response.status_code == 200
    assert pretty_response in response.body.decode('utf-8')


@pytest.mark.parametrize('settings', [dict(render_graphiql=mako_render_graphiql)])
def test_graphiql_mako_renderer(client, pretty_response):
    response = client.get(url_string(query='{test}'), headers={'Accept': 'text/html'})
    assert response.status_code == 200
    assert pretty_response in response.body.decode('utf-8')


def test_graphiql_html_is_not_accepted(client):
    response = client.get(url_string(), headers={'Accept': 'application/json'})
    assert response.status_code == 400


def test_graphiql_get_mutation(client, pretty_response):
    query = 'mutation TestMutation { writeTest { test } }'
    response = client.get(url_string(query=query), headers={'Accept': 'text/html'})
    assert response.status_code == 200
    assert 'response: null' in response.body.decode('utf-8')


@pytest.mark.parametrize('settings', [dict(graphiql_enabled=False)])
def test_graphiql_is_enabled_by_default(client):
    response = client.get(url_string(query='{test}'), headers={'Accept': 'text/html'})
    assert response.status_code == 200
    assert response.content_type == 'application/json'
