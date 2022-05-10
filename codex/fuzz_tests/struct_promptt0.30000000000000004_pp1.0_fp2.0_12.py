import _struct
# Test _struct.Struct
import unittest
import sys
import io
import struct
import copy
import pickle
import test.support
import test.support.script_helper
from test.support import import_helper
from test.support import bigmemtest
from test.support import run_unittest

# The struct module is not available on all platforms.
struct = import_helper.import_module('struct')

# A few tests are skipped on some platforms.
requires_byte_order_little = unittest.skipUnless(sys.byteorder == 'little',
    'test requires little endian byte order')
requires_byte_order_big = unittest.skipUnless(sys.byteorder == 'big',
    'test requires big endian byte order')

# A few tests are skipped on some platforms.
requires_native_byte_order = unittest.skipUnless(sys.byteorder == 'little',
    'test requires native byte order')
requires_other_byte_order = unittest.skipUnless(sys.byteorder == 'big',
    'test requires other byte order')

#
