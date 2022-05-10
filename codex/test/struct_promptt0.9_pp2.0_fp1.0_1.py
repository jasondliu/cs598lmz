import _struct
# Test _struct.Struct.format_size() function.
import test.support
import unittest
from test import mapping_tests
try:
    _struct.pack('=H', 1).decode('ascii')
except LookupError:
    print('LookupError: ascii')
    has_encoding = False
except AttributeError:
    print('AttributeError: pack.decode')
    has_encoding = False
else:
    has_encoding = True


