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
    print codecs.lookup_error('test.lookup').__doc__
    print codecs.lookup_error('test.lookup')(u'abc\u1234def', 0, 1, 'test',
                                             'test.lookup')
    print codecs.lookup_error('test.lookup')(u'abc\u1234def', 0, 1, 'test',
                                             'test.lookup')[0]
    print codecs.lookup_error('test.lookup')(u'abc\u1234def', 0, 1,
