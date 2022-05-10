import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno
import socket
import array
import struct
import select
import time
import platform
import subprocess
import re

from test import support
from test.support import import_module

try:
    import fcntl
except ImportError:
    fcntl = None

if_nametoindex = socket.if_nametoindex
if_indextoname = socket.if_indextoname

class NetworkInterfaceTests(unittest.TestCase):

    def test_if_name_to_index(self):
        # Issue #7995: if_nametoindex() should raise ValueError
        # if the interface is not found.
        self.assertRaises(ValueError, if_nametoindex, 'xyzzy')

