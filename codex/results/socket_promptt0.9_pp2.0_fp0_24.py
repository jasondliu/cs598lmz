import socket
# Test socket.if_indextoname for out-of-range error and IPv6 SIN6_PORT variant
import sys
if sys.version_info[0] >= 3:
   socket_error = OSError
   buffer_type = memoryview
else:
   socket_error = socket.error
import time
import stbt_core as stbt
from _stbt.power import disable_standby_timer
import unittest

def num_bits(n):
    n = n - ((n >> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
    return (((n + (n >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24

class TestStbt(unittest.TestCase):
    def setUp(self):
        self.start = time.time()

    def tearDown(self):
        duration = time.time() - self.start
        if duration > 2:
            print("warning: Test took %.3fs"
