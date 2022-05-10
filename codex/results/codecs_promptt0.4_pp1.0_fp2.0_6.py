import codecs
# Test codecs.register_error()

def handler(exception):
    print("handler called with exception %s" % exception)
    return ("X", exception.end)

codecs.register_error("test.ignore", handler)
codecs.register_error("test.replace", handler)
codecs.register_error("test.xmlcharrefreplace", handler)
codecs.register_error("test.backslashreplace", handler)

def test(encoding):
    print("encoding:", encoding)
    print("ignore:", "abc\xff\u0100".encode(encoding, "test.ignore"))
    print("replace:", "abc\xff\u0100".encode(encoding, "test.replace"))
    print("xmlcharrefreplace:", "abc\xff\u0100".encode(encoding, "test.xmlcharrefreplace"))
    print("backslashreplace:", "abc\xff\u0100".encode(encoding, "test.backslashreplace"))

test("ascii")
test("latin-1")
test("utf-
