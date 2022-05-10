import codecs
# Test codecs.register_error()

import codecs

def replace_errors(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("test.replace", replace_errors)

def test(encoding):
    print '-'*20, encoding
    print u'abc\u1234'.encode(encoding, 'test.replace')
    print u'abc\u1234'.encode(encoding, 'replace')
    print u'abc\u1234'.encode(encoding, 'ignore')
    print u'abc\u1234'.encode(encoding, 'backslashreplace')
    print u'abc\u1234'.encode(encoding, 'xmlcharrefreplace')

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-16-le',
                 'utf-16-be', 'utf-32', '
