import codecs
# Test codecs.register_error
#
import codecs
import unittest

class CodecsRegisterErrorTest(unittest.TestCase):

    def test_register_error(self):
        def my_error_handler(error):
            return "my_error_handler", error.end
        codecs.register_error("test.my_error_handler", my_error_handler)
        self.assertEqual("my_error_handler", codecs.lookup_error("test.my_error_handler"))
        self.assertEqual("my_error_handler", codecs.lookup_error("test.my_error_handler").__name__)
        self.assertEqual("my_error_handler", codecs.lookup_error("test.my_error_handler")("test"))
        self.assertEqual("my_error_handler", codecs.lookup_error("test.my_error_handler")("test", "test"))
