import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecsTest(unittest.TestCase):
    def test_register_error(self):
        def bad_handler(exception):
            raise SystemError
        codecs.register_error('test.bad', bad_handler)
        self.assertRaises(SystemError, codecs.lookup_error('test.bad'),
                          UnicodeEncodeError("ascii", u"\u3042", 0, 1, "ouch"))
        def good_handler(exception):
            return u"\ufffd", exception.end
        codecs.register_error('test.good', good_handler)
        self.assertEqual(codecs.lookup_error('test.good')(
            UnicodeEncodeError("ascii", u"\u3042", 0, 1, "ouch")),
            (u"\ufffd", 1))

def test_main():
    test_support.run_unittest(CodecsTest)
    test_support.reap_children()

if __name
