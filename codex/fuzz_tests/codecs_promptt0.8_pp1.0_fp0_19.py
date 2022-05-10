import codecs
# Test codecs.register_error

class CodecRegistryTest(unittest.TestCase):

    def test_register(self):
        def encode1(input, errors='strict'):
            return ('', 1)
        def decode2(input, errors='strict'):
            return ('', 2)
        #
        codecs.register_error('test.encode1', encode1)
        self.assertEqual(codecs.lookup_error('test.encode1'), encode1)
        codecs.register_error('test.decode2', decode2)
        self.assertEqual(codecs.lookup_error('test.decode2'), decode2)
        #
        codecs.register_error('test.encode1', None)
        self.assertRaises(KeyError, codecs.lookup_error, 'test.encode1')
        codecs.register_error('test.decode2', None)
        self.assertRaises(KeyError, codecs.lookup_error, 'test.decode2')

    def test_lookup(self
