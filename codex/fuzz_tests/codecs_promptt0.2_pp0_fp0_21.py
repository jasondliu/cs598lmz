import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error_handler)

def test(encoding):
    print '-'*20, encoding
    try:
        print 'encode:', repr(unicode('abc\x80def', encoding, 'my_error'))
    except UnicodeError, e:
        print 'encode:', e
    try:
        print 'decode:', repr(unicode('abc\x80def', encoding, 'my_error'))
    except UnicodeError, e:
        print 'decode:', e

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test(encoding)
