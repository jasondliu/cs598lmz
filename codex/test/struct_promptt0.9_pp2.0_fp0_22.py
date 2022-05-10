import _struct
# Test _struct.Struct()
print(_struct.Struct('iif').unpack(_struct.pack('iif', 1, 2, 3.0)))

print(_struct.unpack('iif', _struct.pack('iif', 1, 2, 3.0)))
