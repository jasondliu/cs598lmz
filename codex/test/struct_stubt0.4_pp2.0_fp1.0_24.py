from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i", "")
s.pack(1)

# Test that we can make a Struct from a type
Struct(int)

# Test that we can make a Struct from a type and format
Struct(int, "")

# Test that we can make a Struct from a type, format and size
Struct(int, "", 1)

# Test that we can instantiate a Struct from a type, format and size
Struct.__new__(Struct, int, "", 1)

# Test that we can instantiate a Struct from a type, format and size and call __init__
Struct.__new__(Struct, int, "", 1).__init__(int, "", 1)

# Test that we can instantiate a Struct from a type, format and size and call __init__ and pack
Struct.__new__(Struct, int, "", 1).__init__(int, "", 1).pack(1)

# Test that we can instantiate a Struct from a type, format and size and call __init__ and pack_into
