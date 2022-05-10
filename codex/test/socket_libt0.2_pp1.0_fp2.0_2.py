import socket
import sys
import threading
import time
import traceback

import pytest

from aiohttp import web
from aiohttp.test_utils import make_mocked_coro, make_mocked_request
from aiohttp.web_exceptions import HTTPException
from aiohttp.web_urldispatcher import SystemRoute, UrlDispatcher
from aiohttp.web_urldispatcher import _get_route_name
from aiohttp.web_urldispatcher import _get_route_methods
from aiohttp.web_urldispatcher import _get_route_path
from aiohttp.web_urldispatcher import _get_route_resource
from aiohttp.web_urldispatcher import _get_route_status
from aiohttp.web_urldispatcher import _get_route_host
from aiohttp.web_urldispatcher import _get_route_prefix
from aiohttp.web_urldispatcher import _get_route_handler
