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

# The decode methods on the utf_16_ex, utf_16_le, utf_16_be, utf_32_ex,
# utf_32_le and utf_32_be codecs automatically set the "strict", "ignore",
# "replace" and "xmlcharrefreplace" handlers to the official XML versions
# if they are None.  Registering a new error handler with the name of one
# of these error handlers should replace the official XML version with the
# new error handler.

class UTF16Test(unittest.TestCase):
    def test_xmlcharrefreplace(self):
        utf_8_encoded = "\xed\xa0\x80\xed\xb0\x80\xef\xbf\xbd\xef\xbf\xbd".encode("utf-8")
        utf_8_with_xmlcharrefreplace = "&#xD800;&#xDC00;&#xFFFD;&#xFFFD;".encode("utf-8")
        for codec in "utf_
