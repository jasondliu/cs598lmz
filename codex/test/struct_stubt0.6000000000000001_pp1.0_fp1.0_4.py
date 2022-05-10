from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(b">i")
s.unpack(b"\x12\x34\x56\x78")

# This is the same as:
Struct(b">i").unpack(b"\x12\x34\x56\x78")

# The constructor accepts three optional arguments:
# 1. format string
# 2. callable that converts a sequence of bytes to a tuple (default: Struct.unpack)
# 3. callable that converts a tuple to a sequence of bytes (default: Struct.pack)

# The format string can be passed in the constructor or through the format attribute.
Struct(format=">i").unpack(b"\x12\x34\x56\x78")
Struct.__new__(Struct).__init__(b">i").unpack(b"\x12\x34\x56\x78")

# The format string, the unpack and pack methods can be passed as any combination of
# positional and keyword arguments.
