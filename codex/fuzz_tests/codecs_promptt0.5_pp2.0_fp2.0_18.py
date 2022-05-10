import codecs
# Test codecs.register_error()

import codecs, string, sys

def handler(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u"?", exc.start + 1)
    raise TypeError("don't know how to handle %r" % exc)

def test(encoding):
    print '-' * 50
    print 'Encoding:', encoding
    print 'Encode:  ',
    try:
        print string.join(
            [x.encode(encoding, 'replace') for x in u"abc\u3042\u3044\u3046"],
            ','
        )
    except Exception, why:
        print 'ERROR:', why
    print 'Decode:  ',
    try:
        print string.join(
            [x.decode(encoding, 'replace') for x in "abc\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86"],
            ','
        )
    except Exception, why:
        print 'ERROR:', why
    print 'Register:
