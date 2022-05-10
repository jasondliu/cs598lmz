import _struct
# Test _struct.Struct.unpack_from
#
format = 'hhl'
size = _struct.calcsize(format)
data = array.array('b', b'abcd0123')

print('Format string    :', format)
print('Size of packed   :', size)
print('Data             :', data.tolist())
print()

pos = 0
print('Unpacking from position', pos)
print('Returned Value   :', _struct.unpack_from(format, data, pos))
pos = pos + size
print('After unpack    :', data.tolist())
print('Unpacked bytes   :', data[:pos].tolist())
print()

print('Unpacking from position', pos)
print('Returned Value   :', _struct.unpack_from(format, data, pos))
pos = pos + size
print('After unpack    :', data.tolist())
print('Unpacked bytes   :', data[:pos].tolist())
print()
