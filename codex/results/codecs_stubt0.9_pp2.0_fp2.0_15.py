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

def convert_to():
    return codecs.charmap_encode(REPLACE_WITH_SPACE_CHAR, "test")

class BadDecode(Exception):
    pass

def convert_from(exc):
    if exc.object[exc.start] == b'b'[0]:
        return ("B", exc.start + 1)
    raise BadDecode()

codecs.register_error("test", convert_from)

def fix_unicode(s):
    """Convert all \u1234 escapes to their actual unicode characters.

    Also fixes up tabs and carriage returns in the string.
    """
    if isinstance(s, bytes):
        # Decode to unicode first
        s = s.decode("raw-unicode-escape")
    s = s.replace("\\t", "\t")
    s = s.replace("\\r", "\r")
    if "\\u" not in s:
        # Fastpath
        return s
    def fixup(m):
        hex = m.group(1)
