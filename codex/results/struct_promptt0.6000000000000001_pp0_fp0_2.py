import _struct
# Test _struct.Struct
print(a._struct.Struct('i'))
print(a._struct.Struct('i')(123))

# Test _struct.pack
print(a._struct.pack('i', 123))

# Test _struct.unpack
print(a._struct.unpack('i', a._struct.pack('i', 123)))
print(a._struct.unpack('i', b'\x00\x00\x00{'))
print(a._struct.unpack('i', b'\x00\x00\x00\x7b'))

# Test _struct.calcsize
print(a._struct.calcsize('i'))
print(a._struct.calcsize(b'i'))

# Test _struct.error
try:
    a._struct.pack('i', '123')
except a._struct.error as e:
    print(e)

# Test _struct.iter_unpack
for i in a._struct.iter_unpack('i', a._struct.pack('i', 123)):
    print(i)
