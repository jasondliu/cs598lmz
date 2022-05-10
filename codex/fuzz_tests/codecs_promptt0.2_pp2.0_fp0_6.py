import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error_handler)

def test(encoding):
    print '-'*20
    print 'encoding', encoding
    print 'decode ...'
    print repr(unicode('\xff', encoding, 'my_error'))
    print 'encode ...'
    print repr(unicode('\u1234', 'latin-1').encode(encoding, 'my_error'))

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test(encoding)
