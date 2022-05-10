import _struct
# Test _struct.Struct itself is working.
S = _struct.Struct("I")
print(S.size)
print(S.unpack_from(b"abcd"))

# Test _struct.pack_into
result = []
_struct.pack_into("I", result, 0, 4)

# Test _struct.unpack_from
print(_struct.unpack_from("I", [b"abc", b"def"], 1))

# Test _struct.iter_unpack - using list() to force full evaluation
print(list(_struct.iter_unpack("I", b"abcd")))
