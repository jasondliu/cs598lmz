import codecs
# Test codecs.register_error

import codecs

def my_error(exception):
    return (u'', exception.end)

codecs.register_error('test.myerror', my_error)

def test(encoding):
    print '-'*50
    print 'Encoding :', encoding
    print '-'*50
    print 'encode :', repr(u'\uffff'.encode(encoding, 'test.myerror'))
    print 'decode :', repr(u'\uffff'.encode(encoding).decode(encoding, 'test.myerror'))

for encoding in ['latin-1', 'ascii', 'utf-7', 'utf-8', 'utf-16']:
    test(encoding)
