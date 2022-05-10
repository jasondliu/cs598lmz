import _struct
# Test _struct.Struct()
print('Unpack:', _struct.unpack('>L', b'\x00\x00\x00\x00'))
print('Unpack:', _struct.unpack('>L', b'\x00\x00\x00\x01'))

print('Unpack:', _struct.unpack('>L', b'\x00\x00\x01\x00'))
print('Unpack:', _struct.unpack('>L', b'\x00\x01\x00\x00'))

print('Unpack:', _struct.unpack('>L', b'\x01\x00\x00\x00'))

print('----------------------------------------------------')

print('Pack:', _struct.pack('>L', 1))
print('Pack:', _struct.pack('>L', 256))
print('Pack:', _struct.pack('>L', 65536))

print('----------------------------------------------------')

# 字节序是大端
print('Unpack:', _struct.unpack('>
