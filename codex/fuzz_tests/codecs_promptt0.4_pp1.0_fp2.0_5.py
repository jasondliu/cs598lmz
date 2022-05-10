import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u"", exception.end)

codecs.register_error("test.ignore", handler)

text = u"\u20ac" + u"\x81" + u"\u20ac"

assert codecs.decode(text, "ascii", "test.ignore") == u"\u20ac"
assert codecs.decode(text, "ascii", "test.ignore") == u"\u20ac"
assert codecs.decode(text, "ascii", "test.ignore") == u"\u20ac"

# Test codecs.lookup()

import codecs, sys

assert codecs.lookup(sys.getdefaultencoding()) is codecs.lookup("ascii")

try:
    codecs.lookup("__spam__")
except LookupError:
    pass
else:
    print "expected LookupError"

# Test codecs.open()

import codecs, os

try:

