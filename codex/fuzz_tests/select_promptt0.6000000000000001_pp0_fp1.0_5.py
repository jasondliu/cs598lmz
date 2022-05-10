import select
# Test select.select()
import threading

from typing import List, Optional

from mitmproxy import contentviews
from mitmproxy import exceptions
from mitmproxy import flow
from mitmproxy import http
from mitmproxy import http1
from mitmproxy import io
from mitmproxy import log
from mitmproxy import master
from mitmproxy import proxy
from mitmproxy import websocket
from mitmproxy.utils import strutils

from . import base
from . import flowfilter
from . import dump


class Options:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class DummyServer:
    def __init__(self, master: "master.Master"):
        self.master = master
        self.address = ("localhost", 0)


class DummyProxyServer(DummyServer, proxy.ProxyServer):
    def __init__(self, master: "master.Master"):
        super().__init__(master)
        self.config = proxy.ProxyConfig(
           
