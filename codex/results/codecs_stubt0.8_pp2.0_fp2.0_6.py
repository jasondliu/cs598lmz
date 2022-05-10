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

with open("fixtures/no-bom.utf8", encoding="utf-8") as f:
    raw_contents = f.read()

with open("fixtures/no-bom.utf8", encoding="utf-8", errors="add_one_codepoint") as f:
    contents_with_extra_codepoint = f.read()

with open("fixtures/no-bom.utf8", encoding="utf-8", errors="add_utf16_bytes") as f:
    contents_with_utf16_bytes = f.read()

with open("fixtures/no-bom.utf8", encoding="utf-8", errors="add_utf32_bytes") as f:
    contents_with_utf32_bytes = f.read()

with open("fixtures/no-bom.utf8", encoding="utf-8", errors="surrogatepass") as f:
    contents_with_surrogatepass = f.read()

with open("fixtures/no-bom.utf8", encoding="utf-8", errors
