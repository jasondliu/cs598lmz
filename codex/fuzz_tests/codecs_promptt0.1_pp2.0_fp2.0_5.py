import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test.lookup', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print '%10s  %r' % (encoding, u'\uffff'.encode(encoding, 'test.lookup'))

# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test.lookup', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print '%10s  %r' % (encoding, u'\uffff'.encode(encoding, 'test.lookup'))

# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return
