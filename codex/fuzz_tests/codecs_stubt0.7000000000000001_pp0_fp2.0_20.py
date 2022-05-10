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

data = b'caf\xc3\xa9'

# UTF-16 little endian
try:
    "caf\xe9".encode("utf-16")
except UnicodeEncodeError as exc:
    print("original:", exc.args)
    print("add 1 cp:", ("caf\xe9".encode("utf-16", "add_one_codepoint"),))
    print("add 2 bytes:", ("caf\xe9".encode("utf-16", "add_utf16_bytes"),))

# UTF-16 big endian
try:
    "caf\xe9".encode("utf-16-be")
except UnicodeEncodeError as exc:
    print("original:", exc.args)
    print("add 1 cp:", ("caf\xe9".encode("utf-16-be", "add_one_codepoint"),))
    print("add 2 bytes:", ("caf\xe9".encode("utf-16-be", "add_utf16_bytes"),))

# UTF-32 big end
