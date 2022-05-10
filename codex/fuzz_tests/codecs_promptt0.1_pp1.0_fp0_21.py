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
    print codecs.lookup_error('test.lookup')(u'\ufffe')
    print codecs.lookup_error('test.lookup')(u'\ufffe', 'replace')
    print codecs.lookup_error('test.lookup')(u'\ufffe', 'ignore')
    print codecs.lookup_error('test.lookup')(u'\ufffe', 'backslashreplace')
    print codecs.lookup_error('test.lookup')(u'\ufffe', 'xmlcharrefreplace')
    print codecs.lookup_error('test.lookup')(u'\ufffe', 'test.look
