import select
# Test select.select() with various data structures.
import socket
import os
import urllib
import sys

# Preload the socket module to make sure we have an SOCK_NONBLOCK constant.
import socket

SELECT_TIMEOUT = 0.1

# Select returns scalar int objects, not long ints, so need
# a helper function to cast it.
# XXX - Doesn't work on 64-bit Windows:  http://bugs.python.org/issue1519565
def int_cast(num):
    return int(num)

# According to the man page, the constant underlying select.error is
# supposed to be defined on Unix systems.  On Cygwin, though, it's not,
# so we define it here.
try:
    select.error
except AttributeError:
    if os.name == "posix":
        select.error = socket.error
    elif os.name == "nt" and (sys.version_info.major, sys.version_info.minor) >= (2,5):
        # A Windows-specific exception class
        select.error = Windows
