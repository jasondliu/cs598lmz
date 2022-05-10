import codecs
# Test codecs.register_error()

import codecs

def replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("test.replace", replace_error)

# Test with a unicode string
s = u'\u3042\u3044\u3046\u3048\u304a'
s.encode("euc-jp", "test.replace")

# Test with a byte string
s = '\xa4\xa2\xa4\xa4\xa4\xa6\xa4\xa8\xa4\xaa'
s.decode("euc-jp", "test.replace")

# Test with a unicode string
s = u'\u3042\u3044\u3046\u3048\u304a'
s.encode("euc-jp", "test.replace")

# Test with a byte string
s = '
