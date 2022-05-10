import _struct
# Test _struct.Struct

# Create a struct object
s = _struct.Struct('hhl')

# Get the size of the struct
s.size

# Pack the struct
s.pack(1, 2, 3)

# Unpack the struct
s.unpack(b'\x01\x00\x02\x00\x03\x00\x00\x00')

# Test _struct.calcsize

# Get the size of the struct
_struct.calcsize('hhl')
