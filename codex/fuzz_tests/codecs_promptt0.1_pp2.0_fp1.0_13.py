import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('test.my_error_handler', my_error_handler)

def test(encoding):
    print '-'*20, encoding
    text = u'pi: \u03c0'
    print 'ENCODING:', repr(text.encode(encoding, 'test.my_error_handler'))
    print 'DECODING:', repr(text.encode(encoding, 'test.my_error_handler').decode(encoding))

for encoding in ['ascii', 'latin-1', 'utf-8']:
    test(encoding)

# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('test.my_error_handler', my_error_handler)

def test(encoding):
    print '-'*20, encoding

