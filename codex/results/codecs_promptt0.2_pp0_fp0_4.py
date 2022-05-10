import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print 'my_error_handler called'
    return (u'', exception.end)

codecs.register_error('test.my_error_handler', my_error_handler)

def test(encoding):
    print 'TEST', encoding
    try:
        u'\xff'.encode(encoding)
    except UnicodeEncodeError, err:
        print 'UnicodeEncodeError:', err
        print 'retrying with error handler'
        print u'\xff'.encode(encoding, 'test.my_error_handler')

for encoding in ['ascii', 'latin-1', 'utf-8']:
    test(encoding)

print 'TEST mbcs'
try:
    u'\xff'.encode('mbcs')
except UnicodeEncodeError, err:
    print 'UnicodeEncodeError:', err
    print 'retrying with error handler'
    print u'\xff'.encode('mbcs', 'test
