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
    print codecs.lookup_error('test.lookup').name
    print codecs.lookup_error('test.lookup').__class__
    print codecs.lookup_error('test.lookup')(u'abc', None, None, None, None)
    print codecs.lookup_error('test.lookup')(u'abc', None, None, None, None)
    print codecs.lookup_error('test.lookup')(u'abc', None, None, None, None)
    print codecs.lookup_error('test.lookup')(u'abc', None, None, None, None)
    print codecs.lookup_error('test.lookup')(u'abc', None, None,
