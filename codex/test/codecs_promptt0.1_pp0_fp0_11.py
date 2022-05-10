import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return (u'', exception.end)

codecs.register_error("my_error", my_error_handler)

def test(encoding):
    print("Encoding:", encoding)
    print(codecs.decode("abc\xffdef\xff", encoding, "replace"))
    print(codecs.decode("abc\xffdef\xff", encoding, "ignore"))
    print(codecs.decode("abc\xffdef\xff", encoding, "xmlcharrefreplace"))
    print(codecs.decode("abc\xffdef\xff", encoding, "backslashreplace"))
    print(codecs.decode("abc\xffdef\xff", encoding, "namereplace"))
    print(codecs.decode("abc\xffdef\xff", encoding, "strict"))
    print(codecs.decode("abc\xffdef\xff", encoding, "my_error"))

