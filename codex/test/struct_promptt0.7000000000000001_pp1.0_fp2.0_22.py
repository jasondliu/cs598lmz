import _struct
# Test _struct.Struct() and _struct.unpack()
try:
    import binascii
    import StringIO
    import operator
    import sys
    import tempfile
    import unittest

    def hex(data):
        if sys.version_info < (3,):
            # Python 2.5 has a bug in binascii.b2a_hex().
            # In Python 2.6 and later, the buffer API should be used instead.
            return binascii.hexlify(data)
        else:
            return binascii.b2a_hex(data)
except ImportError:
    # This is not essential.
    pass

import _struct
import sys

def test_struct():
    import string
    # The basic test is to compare pack and unpack results for
    # all format characters with native and standard size.
    for code in _struct.__dict__.keys():
        if code[0] != '_' and len(code) == 1:
            format = code + ' ' * (9 - _struct.calcsize(code))
