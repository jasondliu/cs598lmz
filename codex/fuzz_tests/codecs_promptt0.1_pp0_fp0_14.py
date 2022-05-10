import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print("my_error_handler called with %s" % exception)
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print("testing %s" % encoding)
    try:
        codecs.decode("\xff", encoding, "test.my_error_handler")
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError: %s" % e)

for encoding in ["ascii", "latin-1", "utf-8"]:
    test(encoding)

# Test codecs.register_error with a function that returns a tuple

def my_error_handler(exception):
    print("my_error_handler called with %s" % exception)
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test
