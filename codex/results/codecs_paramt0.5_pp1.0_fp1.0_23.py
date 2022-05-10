import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_encode_decode(self):
        with open('tests/data/utf8.txt', 'r') as f:
            data = f.read()
        encoded = encode(data)
        decoded = decode(encoded)
        self.assertEqual(data, decoded)

    def test_encode_decode_errors(self):
        with open('tests/data/utf8.txt', 'r') as f:
            data = f.read()
        encoded = encode(data, errors='strict')
        decoded = decode(encoded, errors='strict')
        self.assertEqual(data, decoded)

    def test_encode_decode_errors_replace(self):
        with open('tests/data/utf8.txt', 'r') as f:
            data = f.read()
        encoded = encode(data, errors='replace')
        decoded = decode(encoded, errors='replace')
        self.assertE
