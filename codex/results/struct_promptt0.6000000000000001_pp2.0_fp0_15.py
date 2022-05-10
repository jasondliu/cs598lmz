import _struct
# Test _struct.Struct

# Test __new__
assert _struct.Struct("@")
assert _struct.Struct("x")
assert _struct.Struct("@x")
assert _struct.Struct("@P")
assert _struct.Struct("@Px")
assert _struct.Struct("@Px?")
assert _struct.Struct("@Px?b")
assert _struct.Struct("@Px?bh")
assert _struct.Struct("@Px?bhq")
assert _struct.Struct("@Px?bhqQ")
assert _struct.Struct("@Px?bhqQn")
assert _struct.Struct("@Px?bhqQnd")
assert _struct.Struct("@Px?bhqQnds")
assert _struct.Struct("@Px?bhqQndsf")
assert _struct.Struct("@Px?bhqQndsfc")
assert _struct.Struct("@Px?bhqQndsfc?")
assert _struct.Struct("@Px?bhqQndsfc?P")
assert _struct.Struct("@Px
