import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print 'my_error_handler called'
    return (u'', exception.end)

codecs.register_error('test.myerrorhandler', my_error_handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Trying encoding', encoding
    text = u'pi: \u03c0'
    try:
        ascii = text.encode(encoding, 'test.myerrorhandler')
    except UnicodeEncodeError, err:
        print 'ERROR:', err
    else:
        print 'ascii', ascii

# Test codecs.lookup

import codecs

def my_error_handler(exception):
    print 'my_error_handler called'
    return (u'', exception.end)

codecs.register_error('test.myerrorhandler', my_error_handler)

for encoding in ['ascii', 'latin-1', 'utf-8'
