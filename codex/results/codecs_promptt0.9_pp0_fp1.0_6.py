import codecs
# Test codecs.register_error()

### Uncomment this to run the test.
# import os
# if not 'UTF8TEST' in os.environ:
#     os.environ['UTF8TEST'] = 'yes'

import unittest
import utf8test

class BadDecoder(utf8test.BadDecoder):
    def decode(self, input, errors='strict'):
        self.buffer += input
        return 'x' * len(input)

class BadEncoder(utf8test.BadEncoder):
    def encode(self, input, errors='strict'):
        self.buffer += input
        return 'xx' * len(input.encode('latin-1'))

class Test_codecs(utf8test.TestBase, unittest.TestCase):
    encoding = 'utf-8'
    tstring = utf8test.unistr
    codec = codecs.lookup(encoding)

    def test_register_error(self):
        import codecs
        codecs.register_error('test.strict', codec
