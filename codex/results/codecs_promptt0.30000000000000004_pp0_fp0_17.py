import codecs
# Test codecs.register_error
import sys
import unittest
from test import support

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test the codecs.register_error function
        def handler1(exception):
            return ("", exception.end)
        def handler2(exception):
            return ("\uFFFD", exception.end+1)
        def handler3(exception):
            return ("\uFFFD"*(exception.end-exception.start), exception.end)
        def handler4(exception):
            return ("\uFFFD"*(exception.end-exception.start), exception.end+1)
        def handler5(exception):
            return ("\uFFFD"*(exception.end-exception.start), exception.end-1)
        def handler6(exception):
            return ("\uFFFD"*(exception.end-exception.start), exception.end-2)
        def handler7(exception):
            return ("\uFFFD"*(ex
