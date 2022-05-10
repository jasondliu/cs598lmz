import _struct
# Test _struct.Struct
assert _struct.Struct("i").pack(1) == b"\x01\x00\x00\x00"
assert _struct.Struct("i").unpack(b"\x01\x00\x00\x00") == (1,)
# Test _struct.calcsize
assert _struct.calcsize("i") == 4
# Test _struct.error
try:
    _struct.Struct("").pack(1)
except _struct.error as e:
    assert str(e) == "bad char in struct format"

# Test the builtins module
import builtins
assert builtins.abs(-1) == 1
assert builtins.chr(97) == "a"
assert builtins.hex(15) == "0xf"
assert builtins.int("1") == 1
assert builtins.int("1", 10) == 1
assert builtins.len([1, 2, 3]) == 3
