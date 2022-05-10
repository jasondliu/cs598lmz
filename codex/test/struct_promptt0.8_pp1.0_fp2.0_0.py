import _struct
# Test _struct.Struct.format()

def test(args):
    if isinstance(args, str):
        args = (args,)
    fmt = _struct.Struct(*args)
    try:
        rv = fmt.format( *fmt._fmt )
    except ValueError as e:
        rv = e
    print('{}: {}\t=> {}'.format(fmt._fmt, fmt.size, rv))

test('c')
test('b')
test('B')
test('h')
test('H')
test('i')
test('I')
test('l')
test('L')
test('q')
test('Q')
test('f')
test('d')
test('P')

test('cc')
test('bh')
test('iH')
test('lL')
test('qq')
