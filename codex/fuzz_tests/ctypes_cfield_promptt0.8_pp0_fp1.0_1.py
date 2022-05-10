import ctypes
# Test ctypes.CField, it is a little bit different from CField from
# Python/getargs.c, so we'll test them in a separate file.

import unittest
from unittest import mock

from test import support

# This is a wrapper for the CField class from Python/getargs.c
class CFieldWrapper(object):
    def __init__(self, name, ctype, offset, bits, pack, readonly):
        # TODO: add a test with a bitfield
        assert bits == 0
        self.name = name
        self.ctype = ctype
        self.offset = offset
        self.bits = bits
        self.pack = pack
        self.readonly = readonly

        if ctype is ctypes.c_char_p:
            self.dummy_string = b"X" * 4 * ctypes.alignof(ctypes.c_char_p)
            self.dummy_string = ctypes.cast(
                ctypes.addressof(self.dummy_string), ctypes.c_void_p)

    def __get__
