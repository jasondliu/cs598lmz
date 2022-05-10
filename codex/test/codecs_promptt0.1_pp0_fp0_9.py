import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print("Encoding:", encoding)
    print(codecs.decode("abc\xffdef", encoding, "test.my_error_handler"))
    print(codecs.decode("abc\xffdef", encoding, "ignore"))
    print(codecs.decode("abc\xffdef", encoding, "replace"))
    print(codecs.decode("abc\xffdef", encoding, "xmlcharrefreplace"))
    print(codecs.decode("abc\xffdef", encoding, "backslashreplace"))
    print(codecs.decode("abc\xffdef", encoding, "namereplace"))

