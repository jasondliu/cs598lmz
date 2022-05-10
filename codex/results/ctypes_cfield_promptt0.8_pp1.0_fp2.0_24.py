import ctypes
# Test ctypes.CField.from_address()
import os
import sys
from test import test_support
import unittest

class CFuncPtrTestCase(unittest.TestCase):

    def setUp(self):
        if sys.platform not in ('win32', 'cli'):
            self.skipTest('Windows-specific test')

    def test_from_address(self):
        windll.user32.MessageBeep.restype = None
        MessageBeep = ctypes.CFUNCTYPE(None)(windll.user32.MessageBeep)
        addr1 = ctypes.addressof(MessageBeep)
        addr2 = windll.user32.MessageBeep._addr_
        self.assertEqual(MessageBeep, ctypes.CFUNCTYPE(None).from_address(addr1))
        self.assertEqual(MessageBeep, ctypes.CFUNCTYPE(None).from_address(addr2))

    def test_from_address_is_cached(self):
        # Ensure that the same function pointer is returned each time
        # from_
