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
