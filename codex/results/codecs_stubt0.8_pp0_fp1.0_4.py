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

try:
    '\U00010001'.encode("utf-32-le")
except UnicodeEncodeError as exc:
    print("Original error:", exc)
    print("Recovered as:", exc.object.decode("utf-32-le", "add_one_codepoint"))
    print("Recovered as:", exc.object.decode("utf-32-le", "add_utf16_bytes"))
    print("Recovered as:", exc.object.decode("utf-32-le", "add_utf32_bytes"))
