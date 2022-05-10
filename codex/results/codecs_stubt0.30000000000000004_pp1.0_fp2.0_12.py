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

# Test that the codecs module can be imported and that the
# standard error handlers are available

import codecs

def search_function(encoding):
    if encoding == "test.unicode":
        from test import unicode_helper
        return (unicode_helper.streamreader,
                unicode_helper.streamwriter,
                None)
    return None

codecs.register(search_function)

encoding = "test.unicode"

# Test the builtin search function

import codecs

def test(encoding):
    print("trying", encoding)
    try:
        codecs.lookup(encoding)
    except LookupError:
        print("not found")
    else:
        print("found")

test("utf-8")
test("utf-8-sig")
test("utf-16")
test("utf-16-be")
test("utf-16-le")
test("utf-16-be-sig")
test("utf-16-le-sig")
test("utf-
