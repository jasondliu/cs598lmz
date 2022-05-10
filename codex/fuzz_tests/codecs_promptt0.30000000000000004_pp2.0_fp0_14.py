import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Got', exception.__class__
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print repr(unicode('abc\xffdef', encoding, 'test.lookup'))

# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Got', exception.__class__
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print repr(unicode('abc\xffdef', encoding, 'test.lookup'))

# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Got', exception.__
