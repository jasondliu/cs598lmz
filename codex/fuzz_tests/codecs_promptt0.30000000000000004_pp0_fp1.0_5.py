import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print("Exception:", exception)
    return ("[%s]" % exception.object[exception.start:exception.end],
            exception.end)

codecs.register_error("test.ignore", handler)
codecs.register_error("test.replace", handler)
codecs.register_error("test.xmlcharrefreplace", handler)
codecs.register_error("test.backslashreplace", handler)

def test(encoding):
    print("Encoding:", encoding)
    print("Ignore:", codecs.decode("abc\xffdef", encoding, "test.ignore"))
    print("Replace:", codecs.decode("abc\xffdef", encoding, "test.replace"))
    print("XML char ref:",
          codecs.decode("abc\xffdef", encoding, "test.xmlcharrefreplace"))
    print("Backslashreplace:",
          codecs.decode("abc\xffdef", encoding, "test.backslashreplace"))
