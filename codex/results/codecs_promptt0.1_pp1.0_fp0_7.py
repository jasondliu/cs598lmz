import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called'
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding, 'encoding'
    try:
        u'\ud800'.encode(encoding)
    except UnicodeEncodeError, err:
        print 'ERROR:', err

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-16-le',
                 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be']:
    test(encoding)

print 'Trying with test.lookup error handler'
codecs.register_error('test', handler)
for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-16-le',
                 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-
