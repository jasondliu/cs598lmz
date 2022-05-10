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

def check_error_callback(encoding, error_callback, expected_exception):
    try:
        codecs.decode(b"\xFF", encoding, error_callback)
    except UnicodeDecodeError as e:
        assert e.reason == expected_exception
    else:
        assert False, "expected exception not raised"

# Error handlers for UTF-16 and UTF-32 that add one codepoint
# should raise a UnicodeDecodeError.
check_error_callback("utf-16", "add_one_codepoint", "truncated data")
check_error_callback("utf-32", "add_one_codepoint", "truncated data")

# Error handlers for UTF-16 and UTF-32 that add bytes should raise
# a UnicodeDecodeError.
check_error_callback("utf-16", "add_utf16_bytes", "truncated data")
check_error_callback("utf-32", "add_utf32_bytes", "truncated data")

# Error handlers for UTF-16 and UTF-32 that add two bytes
