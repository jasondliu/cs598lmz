import _struct
# Test _struct.Struct

def _test(fmt, expected):
    s = _struct.Struct(fmt)
    got = s.pack(*expected)
    for i in range(len(got)):
        if got[i] != expected[i]:
            print(i, hex(expected[i]), hex(got[i]))
    if got != expected:
        print('Struct(%r).pack(%s) => %r' % (fmt, ', '.join(map(repr, expected)), got))
    else:
        print('Struct(%r).pack(%s) => %r' % (fmt, ', '.join(map(repr, expected)), got), 'ok')

print('sizeof(long)', _struct.calcsize('l'))
print('sizeof(long long)', _struct.calcsize('L'))

_test('hhl', (1, 2, 3))
_test('hhl', (1, 2, -3))
_test('hhl', (1, -2, 3))
_test('hhl', (1
