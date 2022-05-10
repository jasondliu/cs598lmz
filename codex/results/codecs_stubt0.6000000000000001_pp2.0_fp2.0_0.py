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

# Test decoding with different error handlers

# The encoding is chosen to make the decoding fail in the first byte

for enc in ("utf-8", "utf-16", "utf-32"):
    for handler in (None, "xmlcharrefreplace", "ignore", "strict",
                    "surrogateescape", "backslashreplace", "namereplace",
                    "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
        print("'%s' with '%s'" % (enc, handler))
        try:
            codecs.decode("\x80", enc, handler)
        except UnicodeDecodeError as exc:
            print("\t", exc)
        except Exception as exc:
            print("\t", exc)


# Test encoding with different error handlers

# The encoding is chosen to make the encoding fail in the first byte

for enc in ("utf-7", "utf-8", "utf-16", "utf-32"):
    for handler in (None, "xmlcharrefreplace", "ignore",
