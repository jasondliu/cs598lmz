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

s = "\x80"
for encoding in ("utf-8", "utf-16-be", "utf-32-be", "iso8859-1"):
    print("encoding %s." % encoding)
    print("! u.encode(encoding) =", end="")
    try:
        b = s.encode(encoding, "replace")
    except UnicodeEncodeError:  # remove when 3.4 is supported
        print("<UnicodeEncodeError>")
    else:
     
