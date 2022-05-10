import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encode"

codecs.register_error("test.bad_decode", bad_decode)
codecs.register_error("test.bad_encode", bad_encode)

for errors in ('strict', 'ignore', 'replace', 'xmlcharrefreplace',
               'test.bad_decode', 'test.bad_encode'):
    print 'errors =', errors
    print 'u"foo".encode("ascii", errors) =', \
          u"foo".encode("ascii", errors)
    print 'u"\u1234".encode("ascii", errors) =', \
          u"\u1234".encode("ascii", errors)
    print '"foo".decode("ascii", errors) =', \
          "foo".decode("ascii",
