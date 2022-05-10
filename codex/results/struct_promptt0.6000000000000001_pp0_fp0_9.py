import _struct
# Test _struct.Struct class.

f = _struct.Struct("i")

# test __doc__
assert f.__doc__ == "compiled struct object"

# test __new__
assert f.__new__(f, "i") is f

# test invalid format
try:
    _struct.Struct("z")
except ValueError:
    pass
else:
    raise Exception, "expected ValueError"

# test pack
assert f.pack(1) == "1"

# test pack_into
buf = bytearray(4)
f.pack_into(buf, 0, 1)
assert str(buf) == "1"

# test unpack
assert f.unpack("1") == (1,)

# test unpack_from
buf = bytearray("1")
assert f.unpack_from(buf, 0) == (1,)

# test size
assert f.size == 4

# test iter_unpack
buf = bytearray("1")
assert list(f.iter_unpack(buf)) == [(1,)]


