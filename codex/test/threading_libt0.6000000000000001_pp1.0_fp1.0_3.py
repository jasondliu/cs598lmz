import threading
threading.stack_size(67108864)

import aiohttp
import asyncio
import async_timeout
import datetime
import logging
import os
import re
import sys

from aiohttp import web
from aiohttp.client_exceptions import ContentEncodingError
from aiohttp.client_exceptions import ServerDisconnectedError

from urllib.parse import urlencode

from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from mypy_extensions import TypedDict

from py_zipkin.zipkin import create_http_headers_for_new_span
from py_zipkin.zipkin import ZipkinAttrs

from .config import Config
from .config import get_config
from .log import get_logger
from .log import get_zipkin_logger
from .log import log_full_traceback
from .log import log_to_zipkin_span
from .log import log_to_zipkin_trace
