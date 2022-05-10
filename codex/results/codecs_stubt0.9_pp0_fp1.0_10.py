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

with codecs.open("Chn_UTF32_UTF8_UTF16_BE.txt", "r", "utf_16_be", errors="add_utf16_bytes") as f:
    print(f.read())

with codecs.open("Chn_UTF32_UTF8_UTF16_LE.txt", "r", "utf_16_le", errors="add_utf16_bytes") as f:
    print(f.read())

with codecs.open("Chn_UTF32_UTF8_UTF32_BE.txt", "r", "utf_32_be", errors="add_utf32_bytes") as f:
    print(f.read())

with codecs.open("Chn_UTF32_UTF8_UTF32_LE.txt", "r", "utf_32_le", errors="add_utf32_bytes") as f:
    print(f.read())

# This is not working with errors="strict", as expected. When encoding and decoding utf-8
# with python, illegal bytes and missing terminating nulls are being ignored
