import codecs
# Test codecs.register_error()

import codecs
import sys

def handler(exception):
    print("handler:", exception)
    return ("\x00\x00\x00\x00", exception.end)

def search_function(encoding):
    print("search_function:", encoding)
    if encoding != "test.unicode":
        return None
    return (encode, decode, streamreader, streamwriter)

def encode(input, errors="strict"):
    print("encode:", input, errors)
    return ("encoded", len(input))

def decode(input, errors="strict"):
    print("decode:", input, errors)
    return ("decoded", len(input))

def streamreader(stream, errors="strict"):
    print("streamreader:", stream, errors)
    return codecs.StreamReader(stream, errors)

def streamwriter(stream, errors="strict"):
    print("streamwriter:", stream, errors)
    return codecs.StreamWriter(stream, errors)

# Register the search function
