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


class SizeofTestCase(unittest.TestCase):
    """Test _struct.Struct.format_size() function.

    Format strings used for testing (see comments for details):
        'xcc'       # simple format string, char*1 and padding
        'sSpP'      # native size in all formats
        'iihHlLqQfd' # add more types
        'x?'        # bool
        'xp'        # padding for pointers
        'xc0P'      # add char
        '@'         # native alignment (must appear alone)
        '='         # native byteorder, native size, native
