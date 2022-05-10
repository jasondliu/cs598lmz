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
        codecs.decode("\xff", encoding, "test.my_error_handler")
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError:", e)

