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
    print codecs.lookup_error('test.lookup').__module__
    print codecs.lookup_error('test.lookup').__name__
    print codecs.lookup_error('test.lookup').__doc__
    print codecs.lookup_error('test.lookup').__dict__
    print codecs.lookup_error('test.lookup').__class__
    print codecs.lookup_error('test.lookup').__bases__
    print codecs.lookup_error('test.lookup').__mro__
    print codecs.lookup_error('test.lookup').__call__(None, None, None, None, None)
    print codecs.lookup_error('test.look
