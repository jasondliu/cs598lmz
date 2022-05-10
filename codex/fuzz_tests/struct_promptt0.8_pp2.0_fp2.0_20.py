import _struct
# Test _struct.Struct().format_char
print(_struct.Struct('i').format_char) # 'i'
print(_struct.Struct('d').format_char) # 'd'
print(_struct.Struct('P').format_char) # 'P'

# Test _struct.Struct().size
print(_struct.Struct('i').size) # 4
print(_struct.Struct('d').size) # 8

# Test _struct.Struct().pack()
print(_struct.Struct('i').pack(10)) # b'\x0a\x00\x00\x00'
print(_struct.Struct('d').pack(10.0)) # b'@\x00\x00\x00\x00\x00\x00\x00'
print(_struct.Struct('P').pack(10)) # b'\x0a\x00\x00\x00'
print(_struct.Struct('P').pack(10.0)) # b'\x00\x00\x00\x00'

# Test _struct.Struct().unpack()
print(_struct.Struct('i').un
