import codecs
# Test codecs.register_error()
# This test is for the Python 3 case.  Python 2 uses a different
# mechanism for codec error handling.

import codecs

def handler(err):
    print(err)
    return u"", err.start + 1

codecs.register_error("test.strict", handler)

s = "x\x80y\xe0\x80z"

t = codecs.decode(s, "latin1", "test.strict")
assert t == u"x\uFFFDy\uFFFDz"

# Now test with a Unicode string

try:
    t = codecs.decode(u"x\x80y\xe0\x80z", "latin1", "test.strict")
except UnicodeDecodeError:
    pass
else:
    print("did not raise UnicodeDecodeError")

# Test the backslashreplace encoding error handler with
# latin1 and utf-8

def handler(err):
    print(err)
    return u"", err.start + 1

cod
