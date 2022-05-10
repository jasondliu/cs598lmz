import codecs
# Test codecs.register_error
#
# The error handler should be called with 4 arguments:
# - exception instance
# - encoding
# - string
# - startpos
#
# The startpos should be the position of the first byte of the
# character that caused the error.

def handler(exc, enc, s, startpos):
    if exc.__class__ is not UnicodeDecodeError:
        raise TypeError("wrong exception type")
    if enc != "test":
        raise ValueError("wrong encoding")
    if startpos != 1:
        raise ValueError("wrong startpos")
    return (u"\ufffd", startpos+1)

codecs.register_error("test", handler)

s = b"\xff\xff"
u = s.decode("test")
assert u == u"\ufffd\ufffd"

s = b"\xff\xff\xff\xff"
u = s.decode("test")
assert u == u"\ufffd\ufffd\ufffd\ufffd"

s = b"\xff\xff\xff\xff"
u
