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

for name, encoding in [
    ("utf-8", "utf-8"),
    ("utf-16-be", "utf-16-be"),
    ("utf-16-le", "utf-16-le"),
    ("utf-32-be", "utf-32-be"),
    ("utf-32-le", "utf-32-le"),
]:
    for test_name, error_handler, input, expected_output in [
        (
            "short_unicode_string_{}_{}".format(name, error_handler),
            error_handler,
            u"\u00E9\uF900",
            u"\u00E9\u00E9\uF900",
        ),
        (
            "short_unicode_string_encode_error_{}_{}".format(name, error_handler),
            error_handler,
            u"\uD800\uDC00",
            u"\uD800\uDC00",
        ),
        (
            "long_unicode_string_{}_{}".format(
