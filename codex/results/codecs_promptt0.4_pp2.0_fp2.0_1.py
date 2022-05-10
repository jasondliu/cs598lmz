import codecs
# Test codecs.register_error()

import codecs
import encodings

# test codecs.register_error()

def search_function(encoding):
    if encoding == "test.unicode":
        return codecs.lookup(encoding)
    return None

codecs.register(search_function)

def test(encoding):
    print '-'*20, encoding, '-'*20
    # test the first codec
    try:
        u = u"\u3042\u3044"
        print repr(u.encode(encoding)),
        print repr(u.encode(encoding, "strict")),
    except UnicodeError, detail:
        print detail
    try:
        u = u"\u3042\u3044"
        print repr(u.encode(encoding)),
        print repr(u.encode(encoding, "strict")),
    except UnicodeError, detail:
        print detail
    # test the second codec
    try:
        u = u"\u3042\u3044"
        print repr(
