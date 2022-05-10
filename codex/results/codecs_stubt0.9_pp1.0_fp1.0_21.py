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

# UnicodeEncodeError

try:
    u"\ud800".encode("ascii")
except UnicodeEncodeError, e:
    print e, e.start
    print e.object
    print e.reason
    print e.encoding

# UnicodeDecodeError

try:
    "\xe4".decode("utf-8")
except UnicodeDecodeError, e:
    print e, e.start
    print e.object
    print e.reason
    print e.encoding

# UnicodeTranslateError

try:
    u"\ud800".encode("ascii", "ignore")
except UnicodeEncodeError, e:
    print e, e.start
    print e.object
    print e.reason
    print e.encoding

# UnicodeWarning

# TODO

# Registering Error Handlers

try:
    u"\ud800\n".encode("ascii", "add_one_codepoint")
except UnicodeEncodeError, e:
    print e, e.start, repr(
