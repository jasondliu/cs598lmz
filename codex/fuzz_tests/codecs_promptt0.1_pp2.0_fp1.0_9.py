import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print("testing", encoding)
    try:
        codecs.decode(b"\xff", encoding, "test.my_error_handler")
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError:", e)

for encoding in ["ascii", "latin-1", "utf-8"]:
    test(encoding)

# Test codecs.lookup_error

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print("testing", encoding)
    try:
       
