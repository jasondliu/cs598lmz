import codecs
# Test codecs.register_error

import codecs

def replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('test.replace', replace_error)

def test(encoding):
    print '-'*30
    print 'encoding:', encoding
    print 'encode:', repr(u'\u3042\u3044\u3046\u3048\u304a')
    print 'decode:', repr(b'\x82\xa0\x82\xa2\x82\xa4\x82\xa6\x82\xa8')
    print '-'*30
    print
    print 'replace error handler:'
    print '-'*30
    print 'decode:', repr(b'\x82\xa0\x82\xa2\x82\xa4\x82\xa6\x82\xa8')
    print '     :
