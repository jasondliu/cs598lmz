import codecs
# Test codecs.register_error()

import codecs

def my_error(exception):
    print("my_error:", exception)
    return ("", exception.end)

codecs.register_error("test.myerror", my_error)

def test(encoding):
    print("TEST", encoding)
    try:
        codecs.lookup_error("test." + encoding)
    except LookupError:
        print("not supported")
        return
    try:
        u"\u3042".encode(encoding)
    except UnicodeEncodeError as err:
        print("UnicodeEncodeError:", err)
        u"\u3042".encode(encoding, "test." + encoding)
    print()

for encoding in ["strict", "ignore", "replace", "xmlcharrefreplace",
                 "backslashreplace", "namereplace"]:
    test(encoding)

# Test codecs.register_error() with a function that returns a tuple

import codecs

def my_error(exception):
    print("my
