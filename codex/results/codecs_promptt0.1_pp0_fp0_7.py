import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print("my_error_handler called with", exception)
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print("Trying", encoding)
    try:
        u"abc\uDC80def".encode(encoding, "test.my_error_handler")
    except UnicodeEncodeError as err:
        print("UnicodeEncodeError:", err)

test("ascii")
test("latin-1")
test("utf-8")
test("utf-16")
test("utf-32")

# Test codecs.register_error with a function that returns a tuple

def my_error_handler2(exception):
    print("my_error_handler2 called with", exception)
    return (u'', exception.end)

codecs.register_error("test.my_error_handler2", my_error_handler2
