import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    return ("%s" % exception.__class__).encode("ascii"), exception.end

codecs.register_error("test.my_error_handler", handler)

# Test that the handler is used
s = "abc\x80\x81\x82def"
encoding = "ascii"
t = s.encode(encoding, "test.my_error_handler")
if t != b"abc\x80\x81\x82def":
    print("t =", t)
    raise ValueError

# Test that the handler is not used for other encodings
s = "abc\x80\x81\x82def"
encoding = "ascii"
t = s.encode(encoding, "ignore")
if t != b"abcdef":
    print("t =", t)
    raise ValueError

# Test that the handler is not used for other errors
s = "abc\x80\x81\x82def"
encoding = "as
