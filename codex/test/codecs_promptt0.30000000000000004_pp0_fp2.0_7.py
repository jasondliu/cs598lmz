import codecs
# Test codecs.register_error()

import codecs
import sys

def my_error_handler(exception):
    return ("<%s>" % exception.object[exception.start:exception.end],
            exception.end)

def test(codec):
    print("testing", codec)
    text = "abc\x80\x80def"
    try:
        codecs.decode(text, codec)
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError:", e)
    else:
        print("no exception raised")
    codecs.register_error(codec, my_error_handler)
    print("decoding with my_error_handler:", codecs.decode(text, codec))

