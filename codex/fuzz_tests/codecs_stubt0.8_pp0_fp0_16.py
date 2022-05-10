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

def UTF16_BE_LE_CODECS():
    return (( i, "utf-16-%s" % i ) for i in ("be", "le"))

def UTF32_BE_LE_CODECS():
    return (( i, "utf-32-%s" % i ) for i in ("be", "le"))

# utf-16-le and utf-16-be codecs introduced in Python 3.3
try:
    codecs.lookup("utf-16-le")
except LookupError:
    pass
else:
    CODECS = UTF16_BE_LE_CODECS()
    for c in CODECS:
        globals()[c[0].upper() + "_" + "UTF16"] = c[1]

# utf-32-le and utf-32-be codecs introduced in Python 3.3
try:
    codecs.lookup("utf-32-le")
except LookupError:
    pass
else:
    CODECS = UTF32_BE_LE
