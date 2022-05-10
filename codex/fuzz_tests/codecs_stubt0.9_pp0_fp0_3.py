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

# The following codecs have machine generated error handling code.
# See https://docs.python.org/3/library/codecs.html#cruft-to-help-out-omitted-scanner-functions
try:
    codecs.lookup("_unknown")
except LookupError:
    pass

try:
    codecs.lookup("_unknown_error_handler")
except LookupError:
    pass
