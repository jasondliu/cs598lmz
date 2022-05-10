import io
# Test io.RawIOBase: with buffer size, non-blocking and blocking

import io
import random
import socket
import subprocess
import sys
import threading
import unittest

from test.support import TESTFN, run_unittest, import_module, _2G
from test.support.script_helper import assert_python_ok


# tcp_server writes back all bytes it reads, transcoded from UTF-8
# to UTF-16.
stdout, tcp_server = None, None


def setUpModule():
    global stdout, tcp_server
    if sys.platform == "win32":
        # In order to have a Windows-friendly test environment,
        # we'll run the server in a separate process.
        stdout, tcp_server = assert_python_ok("-u", "-c", """
if 1:
    import socket, sys, codecs
    sys.stdout = codecs.getwriter("ascii")(sys.stdout)
    sys.stdin = codecs.getreader("UTF-8")(sys.stdin.detach(), errors="ignore")

