import codecs
# Test codecs.register_error

def search_function(encoding):
    if encoding == "test.unicode.notfound":
        return codecs.lookup(encoding)
    else:
        return None

codecs.register_error("test.notfound", search_function)

for encoding in ["test.unicode.notfound",
                 "test.unicode.notfound-error",
                 "test.unicode.notfound-xmlcharrefreplace",
                 "test.unicode.notfound-ignore",
                 "test.unicode.notfound-replace",
                 ]:
    print encoding,
    try:
        s = u"\udcff".encode(encoding)
        print s
    except UnicodeEncodeError:
        print "UnicodeEncodeError"

import _codecs
# Test _codecs.register_error

def search_function(encoding):
    if encoding == "test.unicode.notfound":
        return codecs.lookup(encoding)
    else:
        return None

_codecs.register
