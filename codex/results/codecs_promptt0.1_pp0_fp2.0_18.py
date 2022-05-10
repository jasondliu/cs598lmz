import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding
    print codecs.lookup_error('test.lookup')
    print codecs.lookup_error('test.lookup').__class__
    print codecs.lookup_error('test.lookup')(u'abc\u1234def', 0, 'test',
                                             encoding, 'test')
    print codecs.lookup_error('test.lookup')(u'abc\u1234def', 1, 'test',
                                             encoding, 'test')
    print codecs.lookup_error('test.lookup')(u'abc\u1234def', 2, 'test',
                                             encoding, 'test')
    print codecs.lookup_error('test.lookup')(u'abc\u1234def', 3, 'test',
                                             encoding, 'test')
