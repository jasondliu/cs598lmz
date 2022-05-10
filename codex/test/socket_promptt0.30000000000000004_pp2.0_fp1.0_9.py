import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno
import platform
import socket
import select
import time
import struct
import subprocess
import re

from test import test_support
from test.test_support import TESTFN, unlink, run_unittest

HOST = test_support.HOST

def is_ipv6_enabled():
    """Return True if IPv6 is enabled on this host."""
    sock = None
    try:
        sock = socket.socket(socket.AF_INET6)
        sock.bind((HOST, 0))
        return True
    except socket.error:
        return False
    finally:
        if sock:
            sock.close()

class NetworkConnectionNoServer(Exception):
    pass

class NetworkConnectionRefused(Exception):
    pass
