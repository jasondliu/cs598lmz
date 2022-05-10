import codecs
# Test codecs.register_error

def search_function(encoding):
    if encoding == 'test.unicode':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

def test(encoding):
    s = 'abc\u1234\u5678def'
    print('Encoding:', encoding)
    print('Original:', repr(s))
    print('Encoded :', repr(s.encode(encoding)))
    print('Decoded :', repr(s.encode(encoding).decode(encoding)))
    print()

test('test.unicode')
test('test.unicode:strict')
test('test.unicode:ignore')
test('test.unicode:replace')
test('test.unicode:backslashreplace')
test('test.unicode:xmlcharrefreplace')
test('test.unicode:namereplace')
test('test.unicode:surrogateescape')
test('test.unicode:surrogatepass')
test('test.unicode:surrogate
