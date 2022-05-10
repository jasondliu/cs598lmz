import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print("TEST", encoding)
    try:
        u"\u3042".encode(encoding, "test.my_error_handler")
    except UnicodeEncodeError as err:
        print("ERROR:", err)

test("ascii")
test("latin-1")
test("utf-8")
test("utf-16")
test("utf-32")
test("iso8859-1")
test("iso8859-15")
test("charmap")

# Test codecs.register_error() with a function that returns a tuple

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return (u'', exception.end)

