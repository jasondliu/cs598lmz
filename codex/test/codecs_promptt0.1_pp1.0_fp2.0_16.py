import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return ("", exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print("TEST", encoding)
    try:
        codecs.decode(b"\xff", encoding, "test.my_error_handler")
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError:", e)

test("ascii")
test("latin-1")
test("utf-8")
test("iso8859-1")
test("iso8859-15")
test("cp1252")
test("charmap")
