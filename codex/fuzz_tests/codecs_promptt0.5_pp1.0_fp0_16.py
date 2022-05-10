import codecs
# Test codecs.register_error()

import codecs, sys

def handler(exc):
    if isinstance(exc, UnicodeDecodeError):
        print 'UnicodeDecodeError:', exc.object[exc.start:exc.end]
    return (u'', exc.end)

codecs.register_error('test.myhandler', handler)

text_str = 'pi: \u03c0'
text_unicode = unicode(text_str, 'ascii', 'test.myhandler')

print 'As unicode :', repr(text_unicode)
print 'As string  :', repr(text_unicode.encode('ascii'))

# Test UnicodeError

import codecs

text = 'abcd'

for encoding in ['ascii', 'latin-1', 'utf-16', 'utf-8']:
    try:
        codecs.lookup(encoding).decode(text)
    except UnicodeError, exc:
        print 'Error decoding %s with %s:' % (repr(text), encoding)
       
