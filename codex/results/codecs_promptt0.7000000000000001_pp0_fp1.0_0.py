import codecs
# Test codecs.register_error()

import test.test_support
import unittest

class RegisterErrorTestCase(unittest.TestCase):
    def setUp(self):
        self.encode_counter = 0
        self.decode_counter = 0
        self.strict_counter = 0
        self.replace_counter = 0
        self.xmlcharrefreplace_counter = 0
        self.backslashreplace_counter = 0

    def test_register_error(self):
        def strict_handler(exception):
            """This handler should never be called"""
            self.strict_counter += 1
            raise exception
        def replace_handler(exception):
            """This handler should never be called"""
            self.replace_counter += 1
            raise exception
        def xmlcharrefreplace_handler(exception):
            """This handler should never be called"""
            self.xmlcharrefreplace_counter += 1
            raise exception
        def backslashreplace_handler(exception):
            """This handler should never be called"""
            self.backslashreplace_counter += 1
            raise
