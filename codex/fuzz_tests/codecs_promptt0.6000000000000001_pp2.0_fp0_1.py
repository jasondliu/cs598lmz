import codecs
# Test codecs.register_error()

def handler(exception):
    print 'Ignoring exception:', exception
    return 0, exception.end

codecs.register_error('test.ignore', handler)

def test(encoding, input):
    print 'Test:', encoding, input
    print '  encode()'
    print '    ', input.encode(encoding, 'test.ignore')
    print '  decode()'
    print '    ', input.decode(encoding, 'test.ignore')

test('ascii', 'abc\xff')
test('ascii', 'abc\xffdef')
test('ascii', 'abc\xffdef\xffghi')
test('ascii', u'abc\xff')
test('ascii', u'abc\xffdef')
test('ascii', u'abc\xffdef\xffghi')

test('latin-1', 'abc\xff')
test('latin-1', 'abc\xffdef')
test('latin-1', 'abc\xffdef\xffghi')
test('l
