import _struct
# Test _struct.Struct

# Test the basic operation of structs.

s = _struct.Struct('i')

# __doc__ attribute
assert s.__doc__ == "Compiled struct object"

# __class__ attribute
assert s.__class__ is _struct.Struct

# __new__()
assert _struct.Struct('i').__new__(_struct.Struct, 'i') is s
assert _struct.Struct('i').__new__(_struct.Struct, 'i') is not s
assert _struct.Struct('i').__new__(_struct.Struct, 'i', 42) is s
assert _struct.Struct('i').__new__(_struct.Struct, 'i', 42) is not s

# __init__()
assert _struct.Struct('i').__init__('i') is None
assert _struct.Struct('i').__init__('i', 42) is None

# __repr__()
assert repr(s) == "Struct('i')"

# __eq__()
assert _struct.Struct('i') == _struct.Struct('i')
assert not _struct
