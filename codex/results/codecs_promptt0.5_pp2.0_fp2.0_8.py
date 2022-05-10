import codecs
# Test codecs.register_error

import codecs

def search_function(encoding):
    if encoding != 'test.searchfunction':
        return None
    return codecs.CodecInfo(
        name='test.searchfunction',
        encode=lambda x, y: x,
        decode=lambda x, y: x,
    )

codecs.register(search_function)

class CodecTest(unittest.TestCase):
    def test_bug1098990(self):
        # _forget_codec() forgets the search function
        codecs.lookup('test.searchfunction')
        self.assertIsNotNone(codecs.lookup('test.searchfunction'))
        codecs._forget_codec('test.searchfunction')
        self.assertIsNone(codecs.lookup('test.searchfunction'))
        codecs.lookup('test.searchfunction')
        self.assertIsNotNone(codecs.lookup('test.searchfunction'))

    def test_bug1092961(self):
        # Make sure that the search function is
