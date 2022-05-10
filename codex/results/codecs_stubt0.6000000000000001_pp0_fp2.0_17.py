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

# UTF-16
# surrogate pair
for surrogate in (0xd800, 0xdfff):
    for error_handler in [None, "strict", "ignore", "replace", "add_one_codepoint"]:
        for byteorder in ['big', 'little']:
            for final in [True, False]:
                print("UTF-16: surrogate=%x, error_handler=%s, byteorder=%s, final=%s" %
                      (surrogate, error_handler, byteorder, final))
                try:
                    codecs.utf_16_decode(bytes([surrogate]), byteorder, final, error_handler)
                except UnicodeDecodeError as exc:
                    print("UnicodeDecodeError:", exc.start, exc.reason)

# UTF-32
# surrogate pair
for surrogate in (0xd800, 0xdfff):
    for error_handler in [None, "strict", "ignore", "replace", "add_one_codepoint"]:
        for byteorder in ['big', 'little']:
            for final
