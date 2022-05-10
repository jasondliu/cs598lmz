import codecs
# Test codecs.register_error().

import sys
import string

ENCODING = 'ascii'

def test(text, enc):
    for name in enc.getregentry():
        print 'Registering replacement_error to encoding', name,
        codecs.register_error(name, replacement_error)
        try:
            u = unicode(text, name, 'replace')
        except UnicodeError:
            raise TestFailed

    e = codecs.lookup(ENCODING)
    print 'Registering replacement_error to encoding', ENCODING,
    codecs.register_error(ENCODING, replacement_error)
    try:
        t = e.encode(unicode(text, e.name, 'strict'), 'replace')
    except UnicodeError:
        raise TestFailed

class replacement_error(object):
    def __init__(self, encoding):
        self.encoding = encoding
    def __call__(self, exc):
        if not isinstance(exc, UnicodeError):
            raise TypeError("don't know how to handle %.400s"
