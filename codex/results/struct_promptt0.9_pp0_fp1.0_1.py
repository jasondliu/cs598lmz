import _struct
# Test _struct.Struct.

struct _test_format ;
X = _struct.Struct('c 4s x f')

assert X.size == 12
assert X.format == _test_format
assertX = _struct.Struct('c 4s x f')
# Ghetto method of checking format
assert struct.unpack(X.format, struct.pack(X.format, b'a', b'test', 0.25)) == (b'a', b'test', 0.25)

# Test .pack() method
assert X.pack(b'a', b'test', 0.25) == struct.pack('c 4s x f', b'a', b'test', 0.25)

# Test .unpack() method
assert X.unpack(b'a    \x00\x00\x00test\x00\x00@\x01\x99\x99\x99\x99\x99\x9a') == (b'a', b'test', 0.25)

# Test .iter_unpack() method
iterable = iter([b'a    \x00
