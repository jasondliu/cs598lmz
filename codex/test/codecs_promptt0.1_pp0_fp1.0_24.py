import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print("my_error_handler: %s" % exception)
    return (u'', exception.end)

codecs.register_error("my_error", my_error_handler)

def test(encoding):
    print("TEST", encoding)
    try:
        u"\u3042".encode(encoding, "my_error")
    except UnicodeEncodeError as e:
        print("UnicodeEncodeError: %s" % e)

for encoding in ["ascii", "latin-1", "iso-8859-1", "iso-8859-15", "utf-8"]:
    test(encoding)

print("Done.")
