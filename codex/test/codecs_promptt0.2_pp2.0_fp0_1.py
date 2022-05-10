import codecs
# Test codecs.register_error

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):
    def test_register_error(self):
        # This tests that the 'register_error' function accepts a
        # unicode argument for the 'name' parameter.
        # See http://bugs.jython.org/issue1847
        codecs.register_error('test.xmlcharrefreplace', codecs.xmlcharrefreplace_errors)

def test_main():
    test_support.run_unittest(CodecsModuleTest)

