import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test', handler)

def test(encoding):
    print encoding
    print codecs.lookup_error('test')
    print codecs.lookup_error('test').__module__
    print codecs.lookup_error('test').__name__
    print codecs.lookup_error('test').__doc__
    print codecs.lookup_error('test').__dict__
    print codecs.lookup_error('test')(u'abc\ud800def', 0, 1, 'test')
    print codecs.lookup_error('test')(u'abc\ud800def', 0, 2, 'test')
    print codecs.lookup_error('test')(u'abc\ud800def', 0, 3, 'test')
    print codecs.lookup_error('test')(u'abc\ud800def', 0, 4, 'test')
   
