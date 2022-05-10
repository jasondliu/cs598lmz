import _struct
# Test _struct.Struct()

import _struct

def test(fmt, input, output):
    s = _struct.Struct(fmt)
    got = s.unpack(s.pack(*input))
    if output != got:
        print fmt, input, got, output

test('=b', (1,), (1,))
test('=b', (-1,), (-1,))
test('=b', (255,), (-1,))
test('=b', (-256,), (0,))
test('=B', (1,), (1,))
test('=B', (255,), (255,))
test('=B', (-1,), (255,))
test('=B', (-256,), (0,))
test('=h', (1,), (1,))
test('=h', (-1,), (-1,))
test('=h', (65535,), (-1,))
test('=h', (-65536,), (0,))
test('=H', (1,), (1,))
test('=H', (65535
