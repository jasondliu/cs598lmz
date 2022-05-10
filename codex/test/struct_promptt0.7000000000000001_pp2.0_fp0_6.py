import _struct
# Test _struct.Struct is not C compatible.
print(_struct.Struct("i").unpack(bytes(4)))  # [0]
print(_struct.Struct("i").unpack(bytes(5)))  # ValueError: unpack requires a bytes object of length 4

# Now test _struct.Struct is C compatible.
print(_struct.Struct("i").unpack(bytes(4), use_c=True))  # [0]
