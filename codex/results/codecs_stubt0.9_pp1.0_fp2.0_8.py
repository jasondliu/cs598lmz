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

def main():
    ENCODINGS = [
        ("utf-8", "replace"),
        ("utf-8", "ignore"),
        ("utf-8", "xmlcharrefreplace"),
        ("utf-8", "backslashreplace"),
        ("utf-8", "namereplace"),
        ("utf-8", "add_one_codepoint"),
        ("utf-8", "surrogateescape"),
        ("utf-16", "add_utf16_bytes"),
        ("utf-32", "add_utf32_bytes"),
    ]


    # Build a basic text object.
    text = chr(0xFFFF) + "Hello World" + chr(0xFFFE)
    t2 = text * 2048

    for encoding, errors in ENCODINGS:
        data = text
        enc_data = text.encode(encoding, errors)

        # Try to decode the encoded string back to unicode.
        try:
            if encoding in ("utf-16", "utf-32", "utf-8-sig"):
                u = enc
