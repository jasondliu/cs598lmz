import codecs
# Test codecs.register_error

class CodecTest(unittest.TestCase):
    codec = 'testcodec'
    encoding = 'test'

    def _do_encode(self, data, expected, **kw):
        self.assertEqual(
            codecs.encode(data, self.codec, self.encoding, **kw),
            expected)

    def _do_decode(self, data, expected, **kw):
        self.assertEqual(
            codecs.decode(data, self.codec, self.encoding, **kw),
            expected)

    def test_simple(self):
        self._do_encode('this is a test', 'this is a test')
        self._do_decode('this is a test', 'this is a test')

    def test_errors(self):
        self.assertRaises(
            UnsupportedError, codecs.encode,
            b'a', self.codec, self.encoding, errors='undefined'
        )
        codecs.encode(b'a', self.codec, self
