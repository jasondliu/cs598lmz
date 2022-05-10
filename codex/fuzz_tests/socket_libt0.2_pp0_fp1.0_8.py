import socket
import sys
import time

import pytest

from aiohttp import web
from aiohttp.test_utils import make_mocked_coro, make_mocked_request
from aiohttp.web import Application, Request, Response, StreamResponse
from aiohttp.web_exceptions import HTTPException, HTTPForbidden, HTTPMethodNotAllowed
from aiohttp.web_exceptions import HTTPNotFound, HTTPRequestEntityTooLarge
from aiohttp.web_exceptions import HTTPServiceUnavailable, HTTPUnauthorized
from aiohttp.web_exceptions import HTTPUnsupportedMediaType, HTTPUpgradeRequired
from aiohttp.web_exceptions import RequestEntityTooLarge, RequestTimeout
from aiohttp.web_exceptions import ServiceUnavailable, TooManyRequests
from aiohttp.web_exceptions import Unauthorized, UpgradeRequired
from aiohttp.web_exceptions import UnsupportedMediaType
from aiohttp.web_urldispatcher import AbstractRoute, UrlDispatcher
from aiohttp.web_urldispatcher import UrlM
