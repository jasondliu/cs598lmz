import select
# Test select.select()
#
# To test select(), we must use non-blocking sockets.
# The easiest way to do this is to set a timeout on the socket.
#
# This test is Linux-specific, because it uses poll() to determine
# whether the socket is ready.
#
# XXX This test doesn't check that readability and writability
# XXX are reported correctly.

import errno
import os
import select
import socket
import sys
import time

try:
    select.poll
except AttributeError:
    raise ImportError("test_select_extra skipped: poll() not available")
try:
    select.POLLIN
except AttributeError:
    raise ImportError("test_select_extra skipped: poll constants not available")

# Some constants
HOST = 'localhost'
PORT = 50007
TIMEOUT = 1.0

# Whether or not to display debugging output
VERBOSE = 0

# Create a non-blocking socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(TIMEOUT)

# Try to
