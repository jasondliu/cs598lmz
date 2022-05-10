import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called'
    return u'', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding, ':',
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, e:
        print e.__class__.__name__, e
    else:
        print 'no exception'

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test(encoding)

print 'Trying lookup_error'

codecs.register_error('test.lookup', codecs.lookup_error('strict'))

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test(encoding)

print 'Trying replace_error'

codecs.register_error('test.lookup', codecs.replace_error('?'))
