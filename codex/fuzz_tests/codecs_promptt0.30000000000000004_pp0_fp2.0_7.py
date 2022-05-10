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

test("ascii")
test("latin-1")
test("iso8859-1")
test("iso8859-15")
test("iso2022_jp")
test("shift_jis")
test("utf-8")
test("utf-16")
test("utf-32")
test("unicode_escape")

