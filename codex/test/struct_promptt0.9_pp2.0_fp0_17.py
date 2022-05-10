import _struct
# Test _struct.Struct()
format = 'hhl'
s = _struct.Struct(format)
data = s.pack(1, 2, 3)
print(s.unpack(data))
print(s.unpack_from(data))
print(s.unpack_from(data, 2))
print(_struct.calcsize(format))
print('-'*30)


# Test pack_into() unpac_into()
data = array('B', b'1234')
print(data)
temp_array = array('B', b'abcdefgh')
print(temp_array)
_struct.pack_into('3h', temp_array, 1, 1, 2, 3)
print(temp_array)
_struct.unpack_from('4h', temp_array, 1)
print(temp_array)
print('-'*30)


# Test _struct.pack()
print(_struct.pack('hhl', 1, 2, 3))
print(_struct.pack('hhl', 3, 2, 1))
print('-'*30)


# Test _struct.unpack
