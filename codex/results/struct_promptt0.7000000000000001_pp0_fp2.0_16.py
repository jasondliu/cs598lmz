import _struct
# Test _struct.Struct.
def test(s, data):
    print s.format, data, '->',
    print s.pack(data)
    print '  ', s.unpack(s.pack(data))
    print '  ', s.unpack_from(s.pack(data), 0)

s = _struct.Struct('i')
test(s, 1)
test(s, -2)

s = _struct.Struct('h')
test(s, 1)
test(s, -2)

s = _struct.Struct('ih')
test(s, (1, 2))
test(s, (1, -2))

s = _struct.Struct('c')
test(s, 'a')
test(s, '\x00')

s = _struct.Struct('cb')
test(s, ('a', 1))
test(s, ('\x00', -2))

test(_struct.Struct('Hi'), (1,))
test(_struct.Struct('Hi'), (1, 0))
test(_struct.Struct('Hi'), (1, 2
