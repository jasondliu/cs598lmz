import _struct
# Test _struct.Struct - issue #13488
# Based on test in test_struct.py

# Test format strings that are not valid C format strings
# (To test the C code itself, use the test_struct module)

import _struct

def test(fmt):
    try:
        s = _struct.Struct(fmt)
    except ValueError:
        pass
    else:
        raise ValueError("expected ValueError for format %r, got %r" % (fmt, s))

test('0')
test('1')
test('2')
test('3')
test('4')
test('5')
test('6')
test('7')
test('8')
test('9')
test('10')
test('#')
test(' ')
test('+')
test('-')
test('.')
test('<')
test('>')
test('@')
test('!')
test('$')
test('%')
test('^')
test('&')
test('*')
test('(')
test(')')
test('~')
test
