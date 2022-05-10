import codecs
# Test codecs.register_error

import codecs
import unittest

class CodecTest(unittest.TestCase):

    def test_register_error(self):
        def my_error_handler(exception):
            return ("my_error_handler", len(exception.object))
        codecs.register_error("test.my_error_handler", my_error_handler)
        self.assertEqual(codecs.lookup_error("test.my_error_handler"),
                         my_error_handler)
        self.assertEqual(codecs.strict_errors, codecs.lookup_error("strict"))
        self.assertEqual(codecs.ignore_errors, codecs.lookup_error("ignore"))
        self.assertEqual(codecs.replace_errors, codecs.lookup_error("replace"))
        self.assertEqual(codecs.xmlcharrefreplace_errors,
                         codecs.lookup_error("xmlcharrefreplace"))
        self.assertEqual(codecs.backslashreplace_errors,
                         codec
