import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return ("", exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print("TEST", encoding)
    try:
        codecs.decode(b"abc\xffdef", encoding)
    except UnicodeDecodeError as exc:
        print("EXCEPTION", exc)

for encoding in ["ascii", "latin-1", "utf-8"]:
    test(encoding)
    test(encoding + ":test.my_error_handler")

# Test codecs.register_error with a callable

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return ("", exception.end)

def test(encoding):
    print("TEST", encoding)
    try:
        codecs.decode(b"abc\xffdef", encoding)
   
