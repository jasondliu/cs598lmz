import _struct
# Test _struct.Struct and _struct.unpack_from
class S(tuple):
    def __add__(self, other):
        return S(self + other)
    __radd__ = __add__

def test_struct_unpack_from():
    # _struct.unpack_from
    s = S(b'abcd')
    assert _struct.unpack_from('>hh', s, 2) == (0x6162, 0x6364)
    assert _struct.unpack_from('hh', s, 2) == (0x6162, 0x6364)
    assert _struct.unpack_from('>hh', s, 2) == (0x6162, 0x6364)
    assert _struct.unpack_from('hh', s) == (0x6162, 0x6364)
    assert _struct.unpack_from('hh', s, 0) == (0x6162, 0x6364)
    assert _struct.unpack_from('hh', s, 1) == (0x6162, 0x6364)
    # if
