import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print("my_error_handler called")
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print("testing", encoding)
    try:
        codecs.decode(b'\xff', encoding, "test.my_error_handler")
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError:", e)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    test(encoding)

# Test codecs.register_error with a tuple

def my_error_handler_tuple(exception):
    print("my_error_handler_tuple called")
    return (u'', exception.end)

