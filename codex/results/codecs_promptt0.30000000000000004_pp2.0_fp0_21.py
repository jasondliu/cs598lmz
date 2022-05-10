import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    return ("", exception.end)

codecs.register_error("test.lookup", handler)

def test(encoding):
    print "Encoding:", encoding
    try:
        u = u"\u3042\u3044\u3046\u3048\u304a"
        s = u.encode(encoding)
        print "Encoded:", s
        print "Decoded:", s.decode(encoding, "test.lookup")
    except LookupError, err:
        print "Lookup error:", err

test("ascii")
test("iso8859-1")
test("iso8859-2")
test("iso8859-15")
test("utf-8")
test("utf-16")
test("utf-16-le")
test("utf-16-be")
test("utf-32")
test("utf-32-le")
test("utf-32-be")
test("unicode-internal")
test("raw-unic
