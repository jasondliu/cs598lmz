import _struct
# Test _struct.Struct.
struct = _struct.Struct('bbh')
assert struct.format == 'bbh'
assert struct.size == struct.size
assert struct.__dict__ == {'format': 'bbh'}
assert repr(struct) == "<struct object at 0x7f4c2b4f4b40>"
struct = _struct.Struct(b'bbh')
assert struct.format == 'bbh'
assert struct.size == struct.size
assert struct.__dict__ == {'format': 'bbh'}
assert repr(struct) == "<struct object at 0x7f4c2b4f4b40>"
struct = _struct.Struct('bbh', 'abc')
assert struct.format == 'abc'
assert struct.size == struct.size
assert struct.__dict__ == {'format': 'abc'}
assert repr(struct) == "<struct object at 0x7f4c2b4f4b40>"
struct = _struct.Struct(b'bbh', b'abc')
assert struct.format == 'abc'
assert struct.size == struct.size

