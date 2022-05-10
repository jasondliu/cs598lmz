import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Got', exception.__class__.__name__
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print repr(unicode('\xff', encoding, 'test.ignore'))
    print repr(unicode('\xff\xff', encoding, 'test.ignore'))
    print repr(unicode('\xff\xff\xff', encoding, 'test.ignore'))
    print repr(unicode('\xff\xff\xff\xff', encoding, 'test.ignore'))
    print

# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Got', exception.__class__.__name__
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

for encoding in ['ascii', '
