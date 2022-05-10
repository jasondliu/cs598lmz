import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('my_error_handler', my_error_handler)

def test(encoding):
    print '%s:' % encoding
    try:
        u = unicode('abc\x80def', encoding, 'my_error_handler')
    except UnicodeError, e:
        print 'ERROR:', e
    else:
        print u.encode(encoding, 'backslashreplace')

for encoding in ['ascii', 'latin-1', 'utf-8']:
    test(encoding)

print 'Done'
