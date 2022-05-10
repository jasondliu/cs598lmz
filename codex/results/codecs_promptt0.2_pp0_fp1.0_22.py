import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Handling %s' % exception.__class__.__name__
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)
codecs.register_error('test.replace', handler)
codecs.register_error('test.xmlcharrefreplace', handler)
codecs.register_error('test.backslashreplace', handler)

def test(encoding):
    print '-'*50
    print encoding
    print '-'*50
    print '%10s: %r' % ('ignore', 'abc\xffdef'.decode(encoding, 'test.ignore'))
    print '%10s: %r' % ('replace', 'abc\xffdef'.decode(encoding, 'test.replace'))
    print '%10s: %r' % ('xmlcharrefreplace', 'abc\xffdef'.decode(encoding, 'test.xmlcharrefreplace'))
    print '%10s: %r' % ('
