import select
import socket
import sys
import threading
import time

import pytest

import aiohttp
from aiohttp import helpers, web
from aiohttp.client import ClientSession
from aiohttp.client_reqrep import ClientRequest
from aiohttp.test_utils import make_mocked_coro, make_mocked_request
from aiohttp.web import Application, Request, Response, StreamResponse
from aiohttp.web_reqrep import Request as BaseRequest
from aiohttp.web_urldispatcher import UrlDispatcher
from aiohttp.web_ws import WebSocketResponse


class TestServer:

    def test_ctor(self):
        app = web.Application()
        with pytest.raises(ValueError):
            web.Server(app, '127.0.0.1', 0, ssl_context=object())

        with pytest.raises(ValueError):
            web.Server(app, '127.0.0.1', 0, backlog=object())

        with pytest.raises(ValueError):
            web.
