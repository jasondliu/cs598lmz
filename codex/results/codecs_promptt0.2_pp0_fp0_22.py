import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print 'my_error_handler called'
    return (u'', exception.end)

codecs.register_error('my_error', my_error_handler)

def test(encoding):
    print 'TEST', encoding
    try:
        unicode('\xff', encoding, 'my_error')
    except UnicodeDecodeError, e:
        print 'UnicodeDecodeError:', e
    print

for encoding in ['ascii', 'latin-1', 'utf-8']:
    test(encoding)
