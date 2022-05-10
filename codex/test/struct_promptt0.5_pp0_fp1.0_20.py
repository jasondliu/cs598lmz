import _struct
# Test _struct.Struct

# Create a struct object
s = _struct.Struct("bbb")
# Create a buffer
b = _struct.pack("bbb", 1, 2, 3)
# Unpack the buffer
print(_struct.unpack("bbb", b))
# Pack the buffer
print(s.pack(1, 2, 3))
# Unpack the buffer
print(s.unpack(b))
# Create a buffer
b = _struct.pack("bbbb", 1, 2, 3, 4)
# Unpack the buffer
print(s.unpack(b))
# Create a buffer
b = _struct.pack("bbbbb", 1, 2, 3, 4, 5)
# Unpack the buffer
print(s.unpack(b))
