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
from mitmproxy.test import taddons
from mitmproxy.test import tflow
from mitmproxy.test import tutils
from mitmproxy.tools import dump


class TestDumpMaster(object):
    def test_dump_app(self):
        with taddons.context() as tctx:
            f = tflow.tflow(resp=True)
            tctx.master.addons.trigger("update", f)
            assert tctx.master.addons.get("dump").dump_app("foo.txt")
            assert os.path.exists("foo.txt")
            os.unlink("foo.txt")


class TestDump(object):
    def test_configure(self):
        d = dump.Dump()
        with pytest.raises(exceptions.OptionsError):
            d.configure(None, dump
