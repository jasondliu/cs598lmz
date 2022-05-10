import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

# try to decode/encode with a non-existing error handler name
try:
    codecs.register_error("test", add_one_codepoint)
except LookupError:
    pass

# try to register an invalid error handler
try:
    codecs.register_error("test", None)
except TypeError:
    pass

# try to register an error handler with non-string arguments
try:
    codecs.register_error("test", add_one_codepoint, None)
except TypeError:
    pass

# try to register an error handler with wrong number of arguments
try:
    codecs.register_error("test", add_one_codepoint, "strict", "ignore")
except TypeError:
    pass

# try to register an error handler with Unicode arguments
try:
    codecs.register_error("test", add_one_codepoint, "strict")
except TypeError:
    pass

# try to register an error handler with keyword arguments
try:
    codecs.register_error("test", add_one_
