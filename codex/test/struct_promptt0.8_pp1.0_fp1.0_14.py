import _struct
# Test _struct.Struct methods using single-argument constructors.

with _struct.Struct('ab') as singlechar:
    assert singlechar.size == 2
    assert singlechar.format == 'ab'
    assert singlechar.unpack_from(b'a') == (97, 98)
    assert singlechar.unpack(b'ab') == (97, 98)
    assert singlechar.unpack_from(b'a', 0) == (97, 98)
    assert singlechar.unpack_from(b'a', 1) == (None, 98)
    assert singlechar.pack_into(b'a', 0, 97, 98) is None
    assert b'a' == b'ab'
    assert singlechar.pack(97, 98) == b'ab'

with _struct.Struct('>') as byte:
    assert byte.size == 1
    assert byte.format == '>'
    assert byte.unpack_from(b'b') == (98,)
    assert byte.unpack(b'b') == (98,)
