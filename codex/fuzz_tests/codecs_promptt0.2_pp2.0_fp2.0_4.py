import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'', exception.end)

codecs.register_error('test.myerror', my_error_handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    try:
        print repr(unicode('\xff', encoding, 'test.myerror'))
    except UnicodeError, err:
        print 'ERROR:', err
    print

# Test codecs.lookup_error()

import codecs

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'', exception.end)

codecs.register_error('test.myerror', my_error_handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    try:
        print repr(unicode('\xff',
