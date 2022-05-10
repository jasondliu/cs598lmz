import _struct
# Test _struct.Struct
_struct.Struct('s').pack(*_struct.Struct('s').unpack(b'xxx'))

x = _struct.Struct('10s 10s')
x.pack(*x.unpack(b'xxxxx xxxxx'))
x = _struct.Struct('20s')
x.pack(*x.unpack(b'xxxxxxxxxxxxxxxxxxxx'))
x = _struct.Struct('21s')
x.pack(*x.unpack(b'xxxxxxxxxxxxxxxxxxxxx'))
x = _struct.Struct('22s')
x.pack(*x.unpack(b'xxxxxxxxxxxxxxxxxxxxxx'))

# Test _struct.calcsize
_struct.calcsize(b'10s 10s')
_struct.calcsize(b'20s')
_struct.calcsize(b'21s')
_struct.calcsize(b'22s')

# Test _struct.__doc__
_struct.__doc__
