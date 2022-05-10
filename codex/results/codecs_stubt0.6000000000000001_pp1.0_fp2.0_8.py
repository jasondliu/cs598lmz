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
    import _multibytecodec as mbc
except ImportError:
    import mbc

coding_map = {
    "utf-8": {
        "teststring": b"a\xe3\x80\x80b",
        "encoded": b"a\xce\xb0\xcc\x80\xce\xb1",
        "decoded": "a\U0003000b",
        "length": 3,
        "errors": ["strict", "ignore", "replace", "xmlcharrefreplace",
                   "backslashreplace", "namereplace", "add_one_codepoint"],
        "errorhandler": "strict",
        "charbuffertype": bytes,
        "max": 0x10ffff,
        "surrogates": False
    },
    "utf-16": {
        "teststring": b"a\xd8\x00\xdc\x00b",
        "encoded": b"a\x00\x00\x01\x00\x00",
        "decoded
