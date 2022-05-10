import codecs
# Test codecs.register_error

def handler(exception):
    print('handler called:', exception)
    return ('?', exception.end)

codecs.register_error('test.myhandler', handler)

def test(name, input, errors='strict'):
    print('Test:', name, 'input:', input, 'errors:', errors)
    print(input.encode('ascii', errors))
    print(input.encode('ascii', 'test.myhandler'))
    print(input.encode('ascii', 'test.myhandler', errors))

test('strict', 'abc\x80')
test('strict', 'abc\x80', 'strict')
test('strict', 'abc\x80', 'ignore')
test('strict', 'abc\x80', 'replace')
test('strict', 'abc\x80', 'test.myhandler')
test('strict', 'abc\x80', 'test.myhandler', 'strict')
test('strict', 'abc\x80', 'test.myhandler', '
