import select
import socket
import sys
import time
import threading
import traceback

import pytest

from mitmproxy import exceptions
from mitmproxy import flow
from mitmproxy import controller
from mitmproxy import proxy
from mitmproxy import options
from mitmproxy import version
from mitmproxy.test import taddons
from mitmproxy.test import tflow
from mitmproxy.test import tutils
from mitmproxy.test import tservers


class TestProxy:
    def test_simple(self):
        p = proxy.Proxy(options.Options())
        p.server = DummyServer(("localhost", 0))
        p.server.start_slave()
        p.shutdown()

    def test_configure(self):
        p = proxy.Proxy(options.Options())
        p.server = DummyServer(("localhost", 0))
        p.server.start_slave()
        p.configure(options.Options(
            mode="reverse:http://localhost:80",
            upstream_server="http://localhost:80"
        ))
        p.shut
