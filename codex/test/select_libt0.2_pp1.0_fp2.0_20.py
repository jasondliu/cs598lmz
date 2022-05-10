import select
import socket
import sys
import threading
import time

import pytest

from mitmproxy import exceptions
from mitmproxy import flow
from mitmproxy import http
from mitmproxy import proxy
from mitmproxy import tcp
from mitmproxy.test import tflow
from mitmproxy.test import tservers
from mitmproxy.tools import dump


class TestDumpMaster(tservers.HTTPProxyTest):
    ssl = True

    def test_dump_master(self):
        f = tflow.tflow(resp=True)
        f.request.host = "address"
        f.request.port = 22
        f.request.scheme = "https"
        f.request.headers["foo"] = "bar"
        f.request.content = b"foo"
        f.response.content = b"bar"
        f.response.headers["foo"] = "bar"
        f.response.headers["mitmproxy"] = "test"
        f.response.stream = True
        f.response.stream_len = 10
