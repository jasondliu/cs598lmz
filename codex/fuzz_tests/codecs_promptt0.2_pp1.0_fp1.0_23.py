import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Error:', exception
    return u'', exception.end

codecs.register_error('test.ignore', handler)
codecs.register_error('test.replace', handler)
codecs.register_error('test.xmlcharrefreplace', handler)
codecs.register_error('test.backslashreplace', handler)

def test(encoding):
    print encoding
    print codecs.decode('abc\xffdef', encoding, 'test.ignore')
    print codecs.decode('abc\xffdef', encoding, 'test.replace')
    print codecs.decode('abc\xffdef', encoding, 'test.xmlcharrefreplace')
    print codecs.decode('abc\xffdef', encoding, 'test.backslashreplace')

test('ascii')
test('latin-1')
test('utf-8')
test('utf-16')
test('utf-32')
test('unicode-escape')
test('raw-unicode-escape')
