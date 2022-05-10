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

