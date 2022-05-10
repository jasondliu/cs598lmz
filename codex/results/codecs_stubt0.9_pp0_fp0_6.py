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

# Commented out because it's an error
#codecs.register_error("unknown_error", 123)

def test_bare_decode(encoding_name):
    print(repr(type(codecs.decode(b'x', encoding_name, 'strict'))))

encoding_names = sorted(codecs.encode.__code__.co_varnames[:codecs.encode.__code__.co_argcount])

for encoding_name in encoding_names:
    if encoding_name in ("errors", "buffering"):
        continue

#    print(encoding_name)
#    print(repr(type(codecs.decode(b'x', encoding_name))))
    try:
        test_bare_decode(encoding_name)
    except:
        print("For codec", encoding_name, "got exception", sys.exc_info())

def test_bare_decode_multi(encoding_name):
    print(repr(type(codecs.decode([
