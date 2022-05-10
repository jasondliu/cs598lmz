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

s = '\xe9' # latin-1 e acute, unicode is u'\u00E9'
try:
    s.decode("ascii")
except UnicodeDecodeError as exc:
    print "Unicode error info:", exc.reason
    print "Position:", exc.start
    print "Ascii value:", s
    print "Using add_one_codepoint to fix error:", exc.object.decode("ascii", "add_one_codepoint")
print

s = '\u20ac' # unicode euro sign, latin-1 is b'\x80'
try:
    s.encode("latin-1")
except UnicodeEncodeError as exc:
    print "Unicode error info:", exc.reason
    print "Position:", exc.start
    print "utf-8 value:", s.encode("utf-8")
    print "Using add_utf16_bytes to fix error:", s.encode("latin-1", "add_utf16_bytes")
print
