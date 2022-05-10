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

for encoding, value, error_handler in [
    ("utf-8", "\xff", "add_one_codepoint"),
    ("utf-16", "\xff", "add_utf16_bytes"),
    ("utf-32", "\xff", "add_utf32_bytes"),
    ("utf-8", "\xff", "ignore"),
    ("utf-16", "\xff", "ignore"),
    ("utf-32", "\xff", "ignore"),
]:
    print("{}:{}:{}".format(encoding, value, error_handler), end="")
    try:
        codecs.decode(value, encoding, error_handler)
    except UnicodeDecodeError as e:
        print(":UnicodeDecodeError")
        print("  start:", e.start)
        print("  end:", e.end)
        print("  reason:", e.reason)
        print("  args:", e.args)
        print("  encoding:", e.encoding)
        print("  object:", e.object)
        print("  end:
