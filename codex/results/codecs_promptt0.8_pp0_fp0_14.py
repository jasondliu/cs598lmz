import codecs
# Test codecs.register_error.

import sys

def handler(ex):
    return "^" + ex.object[ex.start:ex.end] + "^", ex.end

def test():
    e = codecs.register_error("test.strict", handler)
    if e is not None:
        print "register_error should return None"
    s = u"\uD800foobar\uD800".encode("test.strict")
    if s != "^\xff\xfdfoobar^":
        print "test.strict encoding failed"
    try:
        u = s.decode("test.strict")
    except UnicodeError, x:
        print x.__class__.__name__
        print x
    else:
        print "test.strict decoding failed"

test()
