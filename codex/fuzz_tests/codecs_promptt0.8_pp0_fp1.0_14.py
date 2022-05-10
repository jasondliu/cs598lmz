import codecs
# Test codecs.register_error
#
# This test demonstrates that the UnicodeError 'replace' handler
# will be invoked during decoding, and the 'backslashreplace' encoding
# error handler will be invoked during encoding.
# The replacement characters are not tested here.

class Test:
    def test_replace(self):
        assert u"\uDC80\uDC81".encode("ascii", "replace") == \
           "\uDC80\uDC81".encode("ascii")
        assert u"\uDC80\uDC81".encode("ascii", "xmlcharrefreplace") == \
           "&#56384;&#56385;"
        assert u"\uDC80\uDC81".encode("ascii", "backslashreplace") == \
           "\\udc80\\udc81"
        assert u"\uDC80\uDC81".encode("ascii", "namereplace") == \
           "\\N{<control-56384>}\\N{<control-56385>}"

        # Test with errors=None, should behave as
