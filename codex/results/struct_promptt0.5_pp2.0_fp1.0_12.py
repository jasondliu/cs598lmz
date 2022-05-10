import _struct
# Test _struct.Struct.frombytes()
from struct import Struct

from test import support
from test.support import bigaddrspacetest

#
# Test cases
#

class TestStruct:
    def test_format_size_of(self):
        # Test _struct.calcsize()
        for f,s in (('xxxx', 4), ('bxxx', 1), ('hxx', 2), ('i', 4), ('l', 4),
                    ('xxxx', 4), ('bxxx', 1), ('hxx', 2), ('q', 8),
                    ('xxxd', 4), ('c', 1), ('sxx', 2), ('p', _struct.calcsize('P')),
                    ('P', _struct.calcsize('P')), ('Q', 8),
                    ('xxxx', 4), ('bxxx', 1), ('hxx', 2), ('q', 8),
                    ('xxxx', 4), ('bxxx', 1), ('hxx', 2), ('q', 8),
                    ('xxxx', 4), ('bxxx', 1), ('hxx', 2), ('q', 8),
                    ('xxxx', 4), ('
