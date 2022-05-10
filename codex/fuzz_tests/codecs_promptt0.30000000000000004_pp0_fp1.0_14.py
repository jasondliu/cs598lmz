import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Issue #11589: codecs.register_error() is not documented
        # and it is not clear what it is for.
        # This test makes sure that it can be used to replace the
        # default error handler for the 'strict' codec.
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error('strict', handler)
        self.assertEqual(codecs.strict_errors, handler)
        codecs.register_error('strict', None)
        self.assertEqual(codecs.strict_errors, None)

def test_main():
    test.support.run_unittest(CodecsModuleTest)

if __name__ == "__main__":
    test_main()
