import codecs
# Test codecs.register_error()

# This is a test for the register_error() function, to make sure it
# actually works.

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = [ "?" ] * len(exc.object[exc.start:exc.end])
        return (u"".join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("my_replace", my_replace)

s = "\xff"
assert codecs.decode(s, "latin-1", "my_replace") == u"?"

s = "\xff\xff"
assert codecs.decode(s, "latin-1", "my_replace") == u"?"

s = "\xff\xff\xff"
assert codecs.decode(s, "latin-1", "my_replace") == u"?"

s = "\xff\xff\xff\xff"
assert codecs.decode(s,
