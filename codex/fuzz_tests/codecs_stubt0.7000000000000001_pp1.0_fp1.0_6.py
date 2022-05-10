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

# Fuzzing
for i in range(100):
    try:
        codecs.decode("\xF0\xA4\xAD\xA2", "utf-8", "ignore")
        codecs.decode("\xF0\xA4\xAD\xA2", "utf-8", "replace")
        codecs.decode("\xF0\xA4\xAD\xA2", "utf-8", "backslashreplace")
        codecs.decode("\xF0\xA4\xAD\xA2", "utf-8", "namereplace")
        codecs.decode("\xF0\xA4\xAD\xA2", "utf-8", "xmlcharrefreplace")
        codecs.decode("\xF0\xA4\xAD\xA2", "utf-8", "add_one_codepoint")
        codecs.decode("\xF0\xA4\xAD\xA2", "utf-8", "add_
