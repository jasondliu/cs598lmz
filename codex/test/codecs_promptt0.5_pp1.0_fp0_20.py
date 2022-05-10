import codecs
# Test codecs.register_error() and codecs.lookup_error().
import unittest

class TestCodecs(unittest.TestCase):

    def test_register_error(self):
        def errorhandler_import_error(exception):
            raise ImportError
        def errorhandler_lookup_error(exception):
            raise LookupError
        def errorhandler_key_error(exception):
            raise KeyError
        def errorhandler_type_error(exception):
            raise TypeError
        def errorhandler_value_error(exception):
            raise ValueError
        def errorhandler_unicode_error(exception):
            raise UnicodeError
        def errorhandler_unicode_encode_error(exception):
            raise UnicodeEncodeError
        def errorhandler_unicode_decode_error(exception):
            raise UnicodeDecodeError
        def errorhandler_unicode_translate_error(exception):
            raise UnicodeTranslateError
        def errorhandler_test_exception(exception):
            raise TestException
