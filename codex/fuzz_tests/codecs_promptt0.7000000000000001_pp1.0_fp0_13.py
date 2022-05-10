import codecs
# Test codecs.register_error

import codecs

def register_error(exc):
    print "registering error handler for", exc
    return (lambda x: u"<%s>" % x, lambda x: x)

codecs.register_error("test", register_error)

assert unicode("abc\u20ac", "ascii", "test") == u"abc<\u20ac>"
assert unicode("abc\u20ac", "ascii", "replace") == u"abc?"
assert unicode("abc\u20ac", "ascii", "ignore") == u"abc"

# Test codecs.register_error

import codecs

def register_error(exc):
    print "registering error handler for", exc
    return (lambda x: u"<%s>" % x, lambda x: x)

codecs.register_error("test", register_error)

assert unicode("abc\u20ac", "ascii", "test") == u"abc<\u20ac>"
assert unicode("abc\u20ac", "as
