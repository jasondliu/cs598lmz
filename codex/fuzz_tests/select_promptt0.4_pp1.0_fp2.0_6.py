import select
# Test select.select()
#
# This test is not exhaustive.  It only tests the basic functionality and
# error conditions.

import select
import errno
import unittest
import os
import socket
import sys

try:
    import resource
except ImportError:
    resource = None

try:
    import threading
except ImportError:
    threading = None

try:
    import msvcrt
except ImportError:
    msvcrt = None

try:
    import _testcapi
except ImportError:
    _testcapi = None

HOST = 'localhost'

def skip_if_ABSTIME_not_supported():
    """Skip the test if the platform doesn't support ABSTIME."""
    try:
        select.select([], [], [], 0, select.ABSTIME)
    except ValueError:
        raise unittest.SkipTest("platform doesn't support ABSTIME")

class SelectTestCase(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_
