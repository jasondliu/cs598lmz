import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version
from .connection import Connection
from .connection import ConnectionPool
from .connection import SSLConnection
from .connection import SSLConnectionPool
from .connection import VerifiedHTTPSConnection
from .exceptions import (
    ConnectTimeoutError,
    EmptyPoolError,
    HostChangedError,
    MaxRetryError,
    ReadTimeoutError,
    SSLError,
    TimeoutError,
)
from .packages.ssl_match_hostname import match_hostname
from .packages.ssl_match_hostname import CertificateError
from .poolmanager import PoolManager
from .response import HTTPResponse
from .util.request import make_headers
from .util.request import set_request_method
from .util.timeout import Timeout
from .util.url import get_host
from .util.url import parse_url
from .util.url import split_first
from .util.url import Url
