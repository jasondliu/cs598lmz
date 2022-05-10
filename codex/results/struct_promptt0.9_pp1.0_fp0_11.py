import _struct
# Test _struct.Struct
print('_struct.Struct')
_struct.Struct.__doc__
## alignment
_struct.Struct('=cxh').pack(b'a', 2**16 - 1)
# Test _struct.calcsize
print('_struct.calcsize')
_struct.calcsize('cxh')
## alignment
_struct.calcsize('=cxxh')
_struct.calcsize('&^{[')
## alignment
_struct.calcsize('<xxc')
try:
    _struct.calcsize('<')
except TypeError:
    pass
else:
    print('expected TypeError')
# Test _struct.pack
print('struct.pack')
_struct.pack('cxh', b'a', 2**16-1)
## alignment
_struct.pack(b'=cxh', b'a', 2**16-1)
## overlong arguments
_struct.pack('c', b'x' * 1000)
## bad arguments
try:
    _struct.pack('c', b'x' * 2)
except
