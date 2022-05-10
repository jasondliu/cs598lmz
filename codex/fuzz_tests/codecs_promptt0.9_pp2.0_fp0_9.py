import codecs
# Test codecs.register_error

import warnings

class CodecRegressionTest(unittest.TestCase):

    def test_register_error(self):
        # Check the sanity of the baseline error handler.
        #
        # We'll do that by substituting in a new error handler
        # on the fly and seeing what happens.

        encoding = "ascii"

        def myfunc(exc):
            if not isinstance(exc, UnicodeEncodeError):
                self.fail("don't know how to handle %r" % exc)
            if encoding == "replace_other":
                return (u'\uFFFD', exc.end)
            elif encoding == "replace_other_backslashreplace":
                return (u'\\ufffd', exc.end)
            else:
                self.fail("unknown encoding %r" % encoding)

        base_error_function = encodings.lookup_error(encoding)
        try:
            encodings.register_error(encoding, myfunc)

            for orig, expect in (
                # unencodable character
                ("abc\u
