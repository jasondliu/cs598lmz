import socket
# Test socket.if_indextoname, socket.if_nametoindex and socket.if_nameindex
import sys
import unittest

from test import support
from test.support import import_module, TESTFN

is_android = 'ANDROID_DATA' in os.environ

try:
    import fcntl
except ImportError:
    fcntl = None

try:
    import termios
except ImportError:
    termios = None

try:
    import resource
except ImportError:
    resource = None

# Disable tests if we don't have a way to manipulate the non-blocking flag
has_nonblocking = (fcntl is not None)

# Disable tests if we don't have a way to manipulate the close-on-exec flag
has_close_on_exec = (fcntl is not None)

# Disable tests if we don't have a way to manipulate the O_NONBLOCK flag
has_o_nonblock = hasattr(os, "O_NONBLOCK")

# Disable tests if we don't have a way to manipulate the O_ASYNC flag
