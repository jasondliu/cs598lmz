import _struct
# Test _struct.Struct
assert _struct.Struct("@i")("x").x == "x"
assert _struct.Struct("@i")("x").format == "@i"
assert _struct.Struct("@i")("x").size == 4
assert _struct.Struct("@i")("x").pack(1) == "@\x00\x00\x00"
assert _struct.Struct("@i")("x").unpack("@\x00\x00\x00") == [1]
assert _struct.Struct("@i")("x").unpack_from("@\x00\x00\x00\x00\x00\x00\x00", 0) == [1]
assert _struct.Struct("@i")("x").unpack_from("@\x00\x00\x00\x00\x00\x00\x00", 1) == [0]
assert _struct.Struct("@i")("x").unpack("@\x00\x00\x00\x00\x00\x00\x00") == [1, 0, 0]
assert _
