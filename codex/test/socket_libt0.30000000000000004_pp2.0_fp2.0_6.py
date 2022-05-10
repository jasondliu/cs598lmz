import socket
import threading
import time

import pytest

from aiohttp import web
from aiohttp.test_utils import make_mocked_coro
from aiohttp.web_urldispatcher import UrlDispatcher
from aiohttp.web_ws import WebSocketResponse


@pytest.fixture
def make_handler(loop):

    def maker(func):
        return web.RequestHandler(web.Request(web.RawRequestMessage(
            'GET', '/', (1, 1), False, False, b'', None, None, None, None),
            payload=None, loop=loop), web.Response(loop=loop), loop)

    return maker


@pytest.fixture
def app(loop):
    return web.Application(loop=loop)


@pytest.fixture
def handler(app, make_handler):
    return make_handler(app.router.add_route)


