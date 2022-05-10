import codecs
# Test codecs.register_error usage with errors='replace'
class ReplaceTest(unittest.TestCase):

    errorhandler = codecs.replace_errors
    codec = codecs.charmap_build(decoding_table)

    def test_sanity(self):
        self.assertEqual(self.codec.encode('abc'), b'abc')
        self.assertEqual(self.codec.decode(b'def'), 'def')
        self.assertEqual(self.codec.encode('áçeo'), b'aceo')
        self.assertEqual(self.codec.decode(b'st\x01uff'), 'stuff')

    def test_encoding(self):
        self.assertEqual(self.codec.encode('\udcef\udcf0\udcf1',
            'strict'), b'\xff\xff\xff')
        self.assertEqual(self.codec.encode('\udcef\udcf0\udcf1',
            'replace'), b'\xff\xff\xff')
        self
