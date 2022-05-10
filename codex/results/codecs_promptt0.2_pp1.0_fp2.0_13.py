import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'', exception.end)

codecs.register_error('test.my_error_handler', my_error_handler)

def test(encoding):
    print 'TEST:', encoding
    text = u'pi: \u03c0'
    try:
        a = text.encode(encoding, 'test.my_error_handler')
    except UnicodeEncodeError, err:
        print 'ERROR:', err

for encoding in ['ascii', 'latin-1', 'utf-8']:
    test(encoding)
