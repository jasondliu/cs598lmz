import select
# Test select.select for proper socket timeout handling.
import time
import unittest
from test import support
from test.support.script_helper import assert_python_ok
from test.script_helper import assert_python_failure
from test.test_selectors import prepare_for_threads
from test.script_helper import spawn_python
from test.test_builtin import NonClosingBytesIO

# Check that the socket module is there in the first place
import socket

if sys.platform[:3] == 'win':
    error = 10022
else:
    error = errno.EINVAL

try:
    socket.socketpair()
except socket.error:
    SOCKETPAIR_SUPPORTED = False
else:
    SOCKETPAIR_SUPPORTED = True

HAVE_GETNAMEINFO = hasattr(socket, 'getnameinfo')

# Check that the select module is there
try:
    select.select
except AttributeError:
    raise unittest.SkipTest("test skipped because select.select is not defined")
NO_FILEN
