import codecs
# Test codecs.register_error()

def handler(exception):
    print 'Handling %s' % exception.__class__.__name__
    return u'', exception.end

codecs.register_error('test', handler)

def test(encoding):
    print 'Encoding:', encoding
    print 'encode()', repr(u'\u3042\u3044\u3046\u3048\u304a'.encode(encoding, 'test'))
    print 'decode()', repr('\x82\xa0\x82\xa2\x82\xa4\x82\xa6\x82\xa8'.decode(encoding, 'test'))

test('euc-jp')
test('iso2022-jp')
test('shift_jis')
test('utf-8')
test('utf-16')
test('utf-16-le')
test('utf-16-be')
test('utf-32')
test('utf-32-le')
test('utf-32-be')
