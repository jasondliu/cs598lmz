import select
# Test select.select() on sockets.
import time
import unittest
import os
import sys
import errno
from test.support import run_unittest, TESTFN, find_unused_port, bind_port, \
    bind_unix_socket, reap_children, unlink, get_attribute
from test.script_helper import assert_python_ok
from test.script_helper import assert_python_failure
from test.script_helper import assert_python_exit_zero

# Test example from the library reference:  SF bug #622042
HOST = 'localhost'
PORT = find_unused_port()

def socket_pair(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0):
    # We don't want to rely on socket.socketpair() functioning, since
    # some platforms don't support SOCK_NONBLOCK and SOCK_CLOEXEC.
    if family == socket.AF_INET:
        host = HOST
        port = PORT
