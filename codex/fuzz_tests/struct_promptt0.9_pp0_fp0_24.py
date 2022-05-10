import _struct
# Test _struct.Struct().

# .format
assert _struct.Struct('h').format == '<h'
assert _struct.Struct('!h').format == '>h'
assert _struct.Struct('=h').format == '=h'

# __new__
try:
    s = _struct.Struct.__new__(_struct.Struct, 'hi')
except TypeError:
    pass
else:
    raise RuntimeError("_struct.Struct __new__ doesn't raise exception "
                       "when _is_structinstance is false")

# pack
try:
    _struct.Struct('ii').pack()
except TypeError:
    pass
else:
    raise RuntimeError("_struct.pack doesn't raise exception "
                       "when not enough arguments are passed")
try:
    _struct.Struct('i').pack(1, 2, 3)
except TypeError:
    pass
else:
    raise RuntimeError("_struct.pack doesn't raise exception "
                       "when too many arguments are passed")

expected = b'\x00\x00\x00\x00\x00\x
