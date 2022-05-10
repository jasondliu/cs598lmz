import _struct
# Test _struct.Struct
s = _struct.Struct('i')
s.size
s.pack(1)
s.unpack(s.pack(1))
s.unpack_from(buffer(s.pack(1)), 0)
s.pack_into(buffer('12345678'), 4, 2)
s.unpack_from(buffer('12345678'), 4)

# Test _struct.Struct.from_param
def f(s):
    print s.size
    print s.pack(1)
    print s.unpack(s.pack(1))
    print s.unpack_from(buffer(s.pack(1)), 0)
    print s.pack_into(buffer('12345678'), 4, 2)
    print s.unpack_from(buffer('12345678'), 4)
f(_struct.Struct('i'))

# Test _struct.error
try:
    _struct.error
except AttributeError:
    print 'AttributeError'

# Test _struct.calcsize
_struct.calcsize('i')
_struct.calcsize('
