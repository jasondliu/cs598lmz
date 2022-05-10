import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Issue #11471: register_error() should not accept unicode names
        self.assertRaises(TypeError, codecs.register_error, u'ignore')
        self.assertRaises(TypeError, codecs.register_error, u'replace')


def test_main():
    test_support.run_unittest(CodecsModuleTest)

if __name__ == "__main__":
    test_main()
