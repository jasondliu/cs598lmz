import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding
    print codecs.lookup_error('test.lookup')
    print codecs.lookup_error('test.lookup').__name__
    print codecs.lookup_error('test.lookup').__module__
    print codecs.lookup_error('test.lookup')(u'abc', u'\u1234', 1)
    print codecs.lookup_error('test.lookup')(u'abc', u'\u1234', 1, encoding, 'reason')
    print codecs.lookup_error('test.lookup')(u'abc', u'\u1234', 1, encoding, 'reason', 'object')
    print codecs.lookup_error('test.lookup')(u'abc', u'\u1234', 1, encoding, 'reason',
