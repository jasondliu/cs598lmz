import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# test with unicode
for encoding in ('ascii', 'latin-1', 'utf-8'):
    print '%s: %r' % (encoding, unicode('abc\xff', encoding, 'test.ignore'))

# test with str
for encoding in ('ascii', 'latin-1', 'utf-8'):
    print '%s: %r' % (encoding, 'abc\xff'.decode(encoding, 'test.ignore'))
