import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called'
    return u'', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding, 'encoding'
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, err:
        print 'ERROR:', err

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-16-le', 'utf-16-be']:
    test(encoding)

print 'registering error handler for strict codecs'
codecs.register_error('strict', handler)

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-16-le', 'utf-16-be']:
    test(encoding)

print 'registering error handler for replace codecs'
codecs.register_error('replace', handler)

for encoding in ['
