import select
# Test select.select with non-blocking sockets

import errno
import os
import socket
import sys
import time
import unittest
from test import support
from test.support.script_helper import assert_python_ok
from test.support.script_helper import assert_python_failure
from test.script_helper import (
    assert_python_ok, assert_python_failure, spawn_python)


def main():
    # Create a listening socket
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.setblocking(False)
    try:
        lsock.bind(('localhost', 0))
    except OSError as msg:
        # On Windows, socket addresses are reused by default.  If the
        # previous server hasn't completely exited yet, bind() fails
        # with WSAEADDRINUSE.
        if msg.errno != errno.EADDRINUSE:
            raise
        # Wait a second for the server to exit.
        time.sleep(1)
