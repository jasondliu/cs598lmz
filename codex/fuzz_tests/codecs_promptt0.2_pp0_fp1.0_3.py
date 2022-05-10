import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding
    print codecs.lookup_error('test.lookup')
    print codecs.lookup_error('test.lookup').__class__
    print codecs.lookup_error('test.lookup')(u'abc', u'\ufffd', 1, 2, 'test')
    print codecs.lookup_error('test.lookup')(u'abc', u'\ufffd', 1, 2, 'test')[0]
    print codecs.lookup_error('test.lookup')(u'abc', u'\ufffd', 1, 2, 'test')[1]
    print codecs.lookup_error('test.lookup')(u'abc', u'\ufffd', 1, 2, 'test')[2]
    print codecs.lookup_error('test.
