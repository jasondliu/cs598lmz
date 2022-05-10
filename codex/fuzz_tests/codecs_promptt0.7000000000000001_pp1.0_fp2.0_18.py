import codecs
# Test codecs.register_error
import _codecs

# Register codec error handling callback function
def replace_cb(exc):
    if isinstance(exc, UnicodeDecodeError):
        # Replace unencodable '\x81' by '?'
        return (u'?', exc.start + 1)
    else:
        # Cannot handle other exceptions
        raise TypeError("Don't know how to handle %r" % exc)
codecs.register_error("test.replace", replace_cb)

# Encode Unicode string with 'test.replace' error handler
s = u"abc\x81\u1234\u20ac\u8000"
a = s.encode("ascii", "test.replace")
print repr(a)

# Decode byte string with 'test.replace' error handler
b = '\xff\xfeh\x00i\x00\x81\x00\x34\x12\xac\x20\x00\x80'
s = b.decode("utf-16", "test.replace")
print repr(s)

# Register a
