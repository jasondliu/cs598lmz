import _struct
# Test _struct.Struct without format since it could fail while creating
# the instance.
s = _struct.Struct()
# Now test all possible format strings
_struct.Struct('bBhHiIlLqQfdspP')
# The un-pack (special) method
s = _struct.Struct('H')
s.unpack_from(b'abcdef')
# The new module does not have unpack_from()
# XXX:
# bytes.as_bytearray() would be nice, but if the bytes object is very big
# it will create a new bytearray which is not memory-efficient. Creating
# a buffer with PyBuffer_New() is not much better.
# So we need something like bytes.as_bytearray_or_buffer(), or we could
# use a flag argument for bytearray.__init__()...
b = bytearray(b'abcdef')
s.unpack_from(b)
# Same thing, but use a bytes object
s.unpack_from(bytes(b'abcdef'))
# Issue #12623: unpack_from() must
