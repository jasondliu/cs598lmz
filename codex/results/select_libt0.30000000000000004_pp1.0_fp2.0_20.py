import select
import socket
import sys
import threading
import time
import traceback
import unittest

from test import support
from test.support import find_unused_port

# Skip these tests if there is no socket module.
socket = support.import_module('socket')

# Skip these tests if the socket module does not have an AF_UNIX constant.
try:
    socket.AF_UNIX
except AttributeError:
    raise unittest.SkipTest("Platform lacks AF_UNIX")

# Skip these tests if the socket module does not have an SOCK_NONBLOCK
# constant.
try:
    socket.SOCK_NONBLOCK
except AttributeError:
    raise unittest.SkipTest("Platform lacks SOCK_NONBLOCK")

# Skip these tests if the socket module does not have an SOCK_CLOEXEC
# constant.
try:
    socket.SOCK_CLOEXEC
except AttributeError:
    raise unittest.SkipTest("Platform lacks SOCK_CLOEXEC")

# Skip these tests if
