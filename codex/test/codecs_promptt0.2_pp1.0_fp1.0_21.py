import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print("my_error_handler called")
    return (u'', exception.end)

codecs.register_error("my_error", my_error_handler)

def test(encoding):
    print("encoding:", encoding)
    print(codecs.decode("abc\x80\xff", encoding, "my_error"))
    print(codecs.decode("abc\x80\xff", encoding, "replace"))
    print(codecs.decode("abc\x80\xff", encoding, "ignore"))
    print(codecs.decode("abc\x80\xff", encoding, "strict"))

