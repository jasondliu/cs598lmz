import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding, ':',
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e
    else:
        print 'no exception'

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32']:
    test(encoding)

print '\nTest with lookup error handler:'
codecs.register_error('test', 'test.lookup')
for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32']:
    test(encoding)

print '\nTest with strict error handler:'
codecs.register_error('test', 'strict')
for encoding in ['
