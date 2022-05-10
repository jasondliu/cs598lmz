import codecs
# Test codecs.register_error()

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding
    print codecs.lookup_error('test.lookup')
    print codecs.lookup_error('test.lookup').__module__
    print codecs.lookup_error('test.lookup').__name__
    print codecs.lookup_error('test.lookup').__doc__
    print codecs.lookup_error('test.lookup').__dict__
    print codecs.lookup_error('test.lookup').__class__
    print codecs.lookup_error('test.lookup').__class__.__name__
    print codecs.lookup_error('test.lookup').__class__.__module__
    print codecs.lookup_error('test.lookup').__class__.__doc__
    print codecs.lookup_error('test.lookup').__
