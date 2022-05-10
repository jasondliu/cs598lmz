import ctypes
# Test ctypes.CField.from_address

import unittest
from test import support

class CFieldTestCase(unittest.TestCase):

    def test_from_address(self):
        # This is a bit tricky, because we have to find an address
        # that is not part of any Python object.  We do this by
        # allocating a large buffer and then freeing it, so that the
        # address is available for us to use.
        buf = ctypes.create_string_buffer(1024)
        del buf
        addr = ctypes.addressof(buf)
        self.assertRaises(ValueError, ctypes.CField.from_address, addr)

    def test_from_address_with_offset(self):
        buf = ctypes.create_string_buffer(1024)
        del buf
        addr = ctypes.addressof(buf)
        self.assertRaises(ValueError, ctypes.CField.from_address, addr, 1)

    def test_from_address_with_struct(self):
        buf = ctypes.create_string_buffer(
