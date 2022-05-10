import _struct
# Test _struct.Struct with an endian prefix other than "<" or ">"
endianess = {">": "big", "<": "little"}
for fmt, expected in [('@i', 1234), ('=i', 1234), ('!i', 1234)]:
    s = _struct.Struct(fmt)
    assert s.size == 4
    assert s.pack(*(expected,)) == struct.pack(endianess[fmt[0]] + fmt[1:], expected)
    assert s.unpack(s.pack(*(expected,))) == (expected,)
try:
    _struct.Struct('?')
except struct.error:
    pass
else:
    assert False, 'should raise struct.error'
