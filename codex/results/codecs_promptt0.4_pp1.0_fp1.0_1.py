import codecs
# Test codecs.register_error()

import sys

def handler(exception):
    return (u"\ufffd", exception.end)

codecs.register_error("test", handler)

def encode(input, errors="strict"):
    return codecs.utf_8_encode(input, errors)

def decode(input, errors="strict"):
    return codecs.utf_8_decode(input, errors)

def search_function(encoding):
    if encoding != "test":
        return None
    return (encode, decode, None, None)

codecs.register(search_function)

def test(input, errors="strict"):
    print "INPUT:", repr(input)
    print "ENCODING:", errors
    try:
        output = input.encode("test", errors)
        print "ENCODED:", repr(output)
        output = output.decode("test", errors)
        print "DECODED:", repr(output)
    except UnicodeError, e:
        print "ERROR:", e
