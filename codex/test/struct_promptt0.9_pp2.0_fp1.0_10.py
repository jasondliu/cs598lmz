import _struct
# Test _struct.Struct from test_bin.
from .__pypy__ import struct, ext_table
from .__pypy__.builtin import get_exc_value, raises
from .__pypy__.typecell import typecell

def test_struct_calcsize():
    assert _struct.Struct("ci").size == 1 + _struct.calcsize("i")
    assert _struct.Struct("ci").format == "ci"    # don't change the order


def test_struct_pack():
    s = _struct.Struct("l2i")
    assert s.pack(1, 2, 3) == b'\x01' + b'\x00' * 4 + b'\x02' + b'\x00' * 4 + b'\x03' + b'\x00' * 4
    assert s.pack(*range(6)) == b'\x00' * 8 + b'\x01' + b'\x00' * 4 + b'\x02' + b'\x00' * 4


