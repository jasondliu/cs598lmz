import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    return (u"", exception.end)

codecs.register_error("test.my_handler", handler)

def test(encoding):
    print encoding, "->",
    try:
        print codecs.decode(encoding, "test.my_handler")
    except UnicodeDecodeError, e:
        print "UnicodeDecodeError:", e

test("abc\x80\x81\x82")
test("abc\x80\x81\x82\x83")
test("abc\x80\x81\x82\x83\x84")
