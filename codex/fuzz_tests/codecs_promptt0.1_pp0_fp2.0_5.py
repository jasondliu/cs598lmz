import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding, ':',
    try:
        unicode('\xff', encoding, 'test.lookup')
    except UnicodeDecodeError, e:
        print 'ERROR:', e

for encoding in ['ascii', 'latin-1', 'utf-8']:
    test(encoding)

print 'Done'
