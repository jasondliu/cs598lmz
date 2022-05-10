import _struct
# Test _struct.Struct.format_size()

import sys

# Test format_size()

def test(fmt, size, alignment):
    s = _struct.Struct(fmt)
    if s.format_size() != size:
        print('error in', fmt)
        print('returned', s.format_size(), 'instead of', size)
    if s.alignment != alignment:
        print('error in', fmt)
        print('returned', s.alignment, 'instead of', alignment)

test('x', 1, 1)
test('b', 1, 1)
test('B', 1, 1)
test('h', 2, 2)
test('H', 2, 2)
test('i', 4, 4)
test('I', 4, 4)
test('l', 4, 4)
test('L', 4, 4)
test('q', 8, 8)
test('Q', 8, 8)
test('f', 4, 4)
test('d', 8, 8)
test('P', 8, 8)
test('s', 1, 1)
test
