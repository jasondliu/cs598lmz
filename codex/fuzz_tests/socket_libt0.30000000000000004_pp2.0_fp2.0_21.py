import socket
import sys
import threading
import time
import traceback

import pytest

from . import test_utils
from . import utils
from .test_utils import (
    get_open_port,
    run_server,
    run_simple_http_server,
    wait_for_http_server,
    wait_for_server,
)

if sys.version_info >= (3, 7):
    from contextlib import nullcontext
else:
    from contextlib import ExitStack as nullcontext


class TestServer(test_utils.AsyncHTTPTestCase):
    def get_app(self):
        return Application([("/", HelloWorldHandler)])

    def test_start_stop(self):
        self.assertEqual(self.get_http_client().fetch(self.get_url("/")).body, b"Hello, world")
        self.stop()
        self.assertEqual(self.get_http_client().fetch(self.get_url("/")).body, b"Hello, world")

    def test_start_stop
