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
    print codecs.lookup_error('test.lookup').__class__
    print codecs.lookup_error('test.lookup')(u'abc\ud800def')
    print codecs.lookup_error('test.lookup')(u'abc\ud800def', 'replace')
    print codecs.lookup_error('test.lookup')(u'abc\ud800def', 'ignore')
    print codecs.lookup_error('test.lookup')(u'abc\ud800def', 'xmlcharrefreplace')
    print codecs.lookup_error('test.lookup')(u'abc\ud800def', 'backslashreplace')
    print codecs.lookup_error('test.look
