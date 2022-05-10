import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding, ':',
    try:
        u'\u1111'.encode(encoding)
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e
    else:
        print 'no error'

test('ascii')
test('test.lookup')
test('test.lookup,ignore')
test('test.lookup,replace')
test('test.lookup,xmlcharrefreplace')
test('test.lookup,backslashreplace')
test('test.lookup,namereplace')
test('test.lookup,strict')
test('test.lookup,surrogateescape')
test('test.lookup,surrogatepass')
test('test.lookup,test.lookup')
test('test.lookup,test.lookup,
