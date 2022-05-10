import _struct
# Test _struct.Struct.__len__()
s = _struct.Struct('hhl')
# len(s) is number of packed fields
len(s) == 3
# Test _struct.Struct.__init__()
s = _struct.Struct('hhl')
s.format == 'hhl'
s.size == _struct.calcsize('hhl')
s = _struct.Struct('hhhh')
s.format == 'hhhh'
s.size == _struct.calcsize('hhhh')
# Test _struct.Struct.__new__()
s = _struct.Struct('hhl')
# Test _struct.Struct.pack()
s = _struct.Struct('hhl')
t = s.pack(1, 2, 3)
t == b'\x01\x00\x02\x00\x00\x00\x00\x03'
s.pack(1) == b'\x01\x00\x00\x00\x00\x00\x00\x00'
# Test _struct.Struct.unpack()
s = _struct.Struct('hhl
