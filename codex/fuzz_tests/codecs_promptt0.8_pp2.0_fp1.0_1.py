import codecs
# Test codecs.register_error

import codecs
import unittest

def bad_errorhandler(message):
    raise ValueError('codec error')

class CodecTest(unittest.TestCase):
    def test_register_error(self):
        codecs.register_error('test.test1', bad_errorhandler)
        codecs.register_error('test.test2', bad_errorhandler)
        codecs.register_error('test.test1', bad_errorhandler)

    def test_register_error_bad(self):
        self.assertRaises(TypeError,
                          codecs.register_error, 'test.test1', 'xxxx')

def test_main():
    test_support.run_unittest(CodecTest)

if __name__ == "__main__":
    test_main()
