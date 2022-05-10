import weakref

import pytest

from aiohttp import web
from aiohttp.web_exceptions import HTTPForbidden, HTTPMethodNotAllowed
from aiohttp.web_middlewares import _ensure_coroutine, normalize_path_middleware
from aiohttp.web_request import Request
from aiohttp.abc import AbstractAccessLogger
from aiohttp.web_routedef import RouteDef
from aiohttp.web_urldispatcher import SystemRoute, UrlDispatcher
from aiohttp.web_urldispatcher import _check_str


def _make_mocked_coro(return_value=None):
    @asyncio.coroutine
    def coro(*args, **kwargs):
        return return_value

    return coro


class _TestAccessLogger(AbstractAccessLogger):
    def log(self, request, response, time):
        return 'log'


class _TestAccessLoggerFactory:
    def __call__(self, *args):
        return _TestAccessLogger()



