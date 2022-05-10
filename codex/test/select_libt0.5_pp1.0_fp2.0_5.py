import select
import socket
import sys
import time
import traceback
import urllib
import urlparse

import requests

from . import __version__
from .config import Config
from .exceptions import (
    InvalidRequest,
    InvalidResponse,
    InvalidSchema,
    ConnectionClosed,
    ProxyError,
    ServerConnectionError,
)
from .packages.socks import sockssocket
from .packages.socks.socks import PROXY_TYPE_SOCKS4, PROXY_TYPE_SOCKS5
from .packages.socks.sockshandler import SocksiPyHandler
from .packages.urllib3.contrib import socks
from .packages.urllib3.contrib.socks import SOCKSProxyManager
from .packages.urllib3.exceptions import (
    ConnectTimeoutError as _ConnectTimeoutError,
    MaxRetryError,
    ProxyError as _ProxyError,
)
