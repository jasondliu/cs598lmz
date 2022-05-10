import _struct
# Test _struct.Struct.format_size_ok().

def test(fmt):
    try:
        _struct.Struct(fmt)
    except _struct.error:
        print('error:', fmt)
    else:
        print('OK:', fmt)

test('b')
test('l')
test('q')
test('bq')
test('')
test('bqbq')
test('bqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbq')
test('bqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqbqb')
