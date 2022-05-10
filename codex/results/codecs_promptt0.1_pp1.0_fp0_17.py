import codecs
# Test codecs.register_error

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("my_replace", my_replace)

def test(encoding):
    print '-'*20, encoding, '-'*20
    print 'ABCDE'.decode(encoding, 'my_replace')
    print '\xff\xfeA\x00B\x00C\x00D\x00E\x00'.decode(encoding, 'my_replace')
    print '\xff\xfe\x00A\x00\x00B\x00\x00C\x00\x00D\x00\x00E'.decode(encoding, 'my_replace')
    print '\xff\xfe\x00\x00A\x00\x00\x00B\x00\x00\x00C\x00\
