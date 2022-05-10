import _struct
# Test _struct.Struct
#
# NOTE: This test is not exhaustive.  It only tests the lines that
#       are executed by the test_struct module test.

# Basic tests

# size of a packed struct is the same for any format string
assert _struct.calcsize('=i') == _struct.calcsize('=I') == 4

# pack/unpack/unpack_from
assert _struct.pack('=i', 42) == b'*\x00\x00\x00'
assert _struct.pack('=I', 42) == b'*\x00\x00\x00'
assert _struct.unpack('=i', b'*\x00\x00\x00') == (42,)
assert _struct.unpack('=I', b'*\x00\x00\x00') == (42,)
assert _struct.unpack_from('=i', b'*\x00\x00\x00') == (42,)
assert _struct.unpack_from('=I', b'*\x00\x00\x00') == (42
