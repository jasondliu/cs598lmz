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

with open("utf8.txt", "rb") as f:
    utf8_data = f.read()
    print(utf8_data)

with open("utf16.txt", "rb") as f:
    utf16_data = f.read()
    print(utf16_data)

with open("utf32.txt", "rb") as f:
    utf32_data = f.read()
    print(utf32_data)

with open("utf8-nul.txt", "rb") as f:
    utf8_nul_data = f.read()
    print(utf8_nul_data)

with open("utf16-nul.txt", "rb") as f:
    utf16_nul_data = f.read()
    print(utf16_nul_data)

with open("utf32-nul.txt", "rb") as f:
    utf32_nul_data = f.read()
    print(utf32_nul_data)

print(text_
