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

# Test with surrogate pairs
for encoding in "utf-16", "utf-16-le", "utf-16-be", "utf-32", "utf-32-le", "utf-32-be":
    for error_handler in "strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes":
        print("Testing decode with %s and error handler %s" % (encoding, error_handler))
        try:
            codecs.decode("\ud800\udc00\ud800\udc00", encoding, error_handler)
        except UnicodeDecodeError:
            print("UnicodeDecodeError")

# Test with a single unpaired surrogate
for encoding in "utf-16", "utf-16-le", "utf-16-be", "utf-32", "utf-32-le", "utf-32-be":
    for error_handler in "strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add
