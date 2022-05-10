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

# Error handling should affect encoding and decoding
for name, (decoding, encoding) in (
        ("add_one_codepoint", ("replace", "replace")),
        ("add_utf16_bytes", ("ignore", "backslashreplace")),
        ("add_utf32_bytes", ("ignore", "xmlcharrefreplace"))):
    for func, args in (
            (codecs.decode, (b"\xff", "ascii", decoding)),
            (codecs.encode, ("\uffff", "ascii", encoding))):
        try:
            res = func(*args)
        except UnicodeError:
            pass
        else:
            print("%r should have raised an exception" % func.__name__)

# XXX
print(codecs.encode(b'abc', 'ascii'))
print(codecs.encode(b'abc', 'ascii', 'add_one_codepoint'))
print(codecs.encode(b'abc', 'ascii', 'add_utf16
