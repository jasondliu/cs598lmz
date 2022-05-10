import _struct
# Test _struct.Struct()
s = _struct.Struct('i')
s.size
s.format
s = _struct.Struct('i')
format = s.format
'i'
s.size
_struct.calcsize('i')
format = s.format
s.size
_struct.calcsize('i')
# Test Struct.pack()
s = _struct.Struct('i')
data = s.pack(-1)
len(data)
s.size
data = s.pack(-1)
list(_struct.unpack(format, data))
data + 'junk'
s.pack(-1)
# Test Struct.unpack_from()
s = _struct.Struct('hxh')
len(s.pack(1, 2))
# dummy buffer
buf = '12345678'
# offset in bytes from beginning of buffer
offset = 4
trans = s.unpack_from(buf, offset=offset)
trans
type(trans)
# Test Struct.unpack()
type(_struct.unpack("b", "a"))
type(_struct.unpack("b", "
