import socket
# Test socket.if_indextoname

import os, sys
import unittest
from test.support import is_android
from test.support import run_unittest
import errno

from socket import (
    if_nametoindex, if_indextoname, if_nameindex, if_nametoindex,
    socket, AF_INET, SOCK_DGRAM)

try:
    import fcntl
except ImportError:
    fcntl = None


# We need to test a variant of socket.if_nameindex() that works on the
# current platform and can be called reliably.
