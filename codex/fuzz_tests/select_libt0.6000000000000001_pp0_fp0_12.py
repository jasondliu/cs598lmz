import selectors
import threading
import time
import traceback
import uuid

import grpc
import pytest

from google.protobuf import empty_pb2

from tests.stub.config import (
    HTTP_PORT,
    HTTP_SERVER_HOST,
    HTTPS_PORT,
    HTTPS_SERVER_HOST,
    HTTP_PROXY_PORT,
    HTTPS_PROXY_PORT,
    HTTP_CONTROL_PORT,
    HTTPS_CONTROL_PORT,
)
from tests.stub.config_utils import get_config
from tests.stub.utils import get_free_port

from mitmproxy import exceptions
from mitmproxy.io.tcp import tcp_read, tcp_write

from mitmproxy.addons import clientplayback
from mitmproxy.addons import proxyauth
from mitmproxy.addons import readfile
from mitmproxy.addons import serverplayback
from mitmproxy.addons import stickyauth
from mitmproxy.addons import termlog
from mitmproxy.addons import view
from mitmproxy.
