import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print("my_error_handler: %r" % (exception,))
    return (u'', exception.end)

codecs.register_error("my_error", my_error_handler)

def test(encoding):
    print("TEST", encoding)
    try:
        u"\u3042".encode(encoding)
    except UnicodeEncodeError as e:
        print("UnicodeEncodeError:", e)
    try:
        b"\xff".decode(encoding)
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError:", e)

for encoding in ["ascii", "latin-1", "utf-8"]:
    test(encoding)

print("registering error handler")
codecs.register_error("my_error", my_error_handler)

for encoding in ["ascii", "latin-1", "utf-8"]:
    test(encoding)

