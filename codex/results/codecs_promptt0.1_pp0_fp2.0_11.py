import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called'
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

def test(encoding):
    print 'Trying', encoding
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e
        print 'retval', repr(e.object), 'end', e.end

for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-16-be',
                 'utf-16-le', 'utf-32', 'utf-32-be', 'utf-32-le',
                 'raw_unicode_escape', 'unicode_escape', 'unicode_internal'):
    test(encoding)

print 'Trying test.lookup'
test('test.lookup')
