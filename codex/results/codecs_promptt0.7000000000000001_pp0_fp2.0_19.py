import codecs
# Test codecs.register_error, and implicit register_error via a CodecInfo
# object, with the 'replace' error handler.

import test.test_support
import unittest

# UnicodeError is an alias for ValueError
def _check_exception(exception):
    if isinstance(exception, UnicodeError):
        return True
    if not isinstance(exception, ValueError):
        return False
    msg = exception.args[0]
    return (msg.startswith("unexpected code_string character") or
            msg.startswith("codec can't decode byte"))

class TestReplace(unittest.TestCase):
    def test_search_function(self):
        import codecs
        def custom_replace(exception):
            # \uFFFD is the Unicode replacement character
            return (u'\uFFFD', exception.end)
        codecs.register_error("test.replace", custom_replace)
        # build a codec with a custom error handler
        mycodec = codecs.lookup("test.replace")
        self.assertEquals(mycodec
