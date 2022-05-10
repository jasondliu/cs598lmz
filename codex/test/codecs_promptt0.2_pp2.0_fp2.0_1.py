import codecs
# Test codecs.register_error()

import codecs

def my_error(exception):
    print("my_error:", exception)
    return ("", exception.end)

codecs.register_error("test.myerrorhandler", my_error)

def test(encoding):
    print("TEST", encoding)
    try:
        codecs.decode("abc\x80\x80\xc0", encoding, "test.myerrorhandler")
    except UnicodeError as exc:
        print("EXCEPTION:", exc)

