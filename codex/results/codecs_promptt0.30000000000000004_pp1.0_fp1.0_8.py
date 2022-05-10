import codecs
# Test codecs.register_error()

import codecs

def handler(exc):
    return (u"", exc.end)

codecs.register_error("test", handler)

def test(encoding):
    print '-'*20, encoding
    try:
        u"\x81".encode(encoding)
    except UnicodeEncodeError, err:
        print 'UnicodeEncodeError:', err
        print 'encoding:', err.encoding
        print 'reason:', err.reason
        print 'object:', err.object
        print 'start:', err.start
        print 'end:', err.end
    print u"\x81".encode(encoding, "test")

for encoding in ["ascii", "iso-8859-1", "iso-8859-15", "cp1252", "mac-roman",
                 "utf-8", "utf-16", "utf-16-be", "utf-16-le", "utf-32",
                 "utf-32-be", "utf-32-le"]:
    test(enc
