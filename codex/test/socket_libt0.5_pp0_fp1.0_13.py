import socket

import pytest

from aiohttp import web
from aiohttp.test_utils import make_mocked_coro
from aiohttp.web_reqrep import Request, StreamResponse


@pytest.fixture
def resp():
    return StreamResponse(status=200)


def test_ctor(resp):
    assert 200 == resp.status
    assert resp.reason is None
    assert resp.headers == resp._headers
    assert resp.content is None
    assert resp.keep_alive is None
    assert resp.charset is None
    assert resp.content_type == 'text/plain'
    assert resp.content_length is None
    assert resp.last_modified is None
    assert resp.access_control_allow_origin is None
    assert resp.access_control_allow_credentials is None
    assert resp.access_control_max_age is None
    assert resp.access_control_allow_methods is None
    assert resp.access_control_allow_headers is None
    assert resp.vary is None
    assert resp.cache_control
