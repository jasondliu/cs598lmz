import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print "my_error_handler:", exception
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print "TEST", encoding
    try:
        u"\u3042".encode(encoding, "test.my_error_handler")
    except UnicodeEncodeError, e:
        print "UnicodeEncodeError:", e

for encoding in ["ascii", "latin-1", "utf-8", "utf-16"]:
    test(encoding)

# Test codecs.lookup

import codecs

def my_encode(input, errors="strict"):
    return (input.upper(), len(input))

def my_decode(input, errors="strict"):
    return (input.lower(), len(input))

codecs.register(lambda name: codecs.CodecInfo(
       
