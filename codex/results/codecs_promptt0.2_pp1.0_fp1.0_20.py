import codecs
# Test codecs.register_error()

def handler(exception):
    print 'Handling %s' % exception.__class__.__name__
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)
codecs.register_error('test.replace', handler)
codecs.register_error('test.xmlcharrefreplace', handler)
codecs.register_error('test.backslashreplace', handler)

def test(encoding):
    print '-'*50
    print 'Encoding:', encoding
    print 'Encode:', repr(u'\u3042\u3044\u3046\u3048\u304a')
    print 'Decode:', repr('\x82\xa0\x82\xa2\x82\xa4\x82\xa6\x82\xa8')
    print '-'*50
    print 'strict'
    print '-'*50
    print 'encode()', repr(u'\u3042\u3044\u3046\u3048\u
