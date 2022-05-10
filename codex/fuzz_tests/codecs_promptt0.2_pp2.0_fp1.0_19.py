import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print 'my_error_handler called'
    return (u'', exception.end)

codecs.register_error('test.myerrorhandler', my_error_handler)

def test(encoding):
    print 'TEST', encoding
    try:
        u'\xff'.encode(encoding, 'test.myerrorhandler')
    except UnicodeEncodeError, err:
        print 'ERROR:', err

for encoding in ['latin-1', 'ascii', 'utf-8']:
    test(encoding)

# Test codecs.register_error with a tuple

def my_error_handler(exception):
    print 'my_error_handler called'
    return (u'', exception.end)

codecs.register_error('test.myerrorhandler', (my_error_handler, 'replace'))

def test(encoding):
    print 'TEST', encoding
    try:
        u'\xff'.encode(encoding,
