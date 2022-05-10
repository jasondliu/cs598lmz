import codecs
# Test codecs.register_error


class CodecRegistrableTest(unittest.TestCase):
    def setUp(self):
        self.encoding = "test.registerableencoding"
        self.lower_encoding = self.encoding.lower()
        self.s = "test_registration_output\N{LATIN SMALL LETTER SHARP S}"
        self.ucs = self.s.encode('utf-8')
        self.bad_chars = "X"
        self.bad_ucs = self.bad_chars.encode('utf-8')
        self.replace_chars = "?"
        self.replace_ucs = self.replace_chars.encode('utf-8')
        self.default_ucs = self.bad_ucs


class CodecsModuleTest(CodecRegistrableTest):

    def test_register_error(self):
        errors.register_error('test.registerableencoding', codecs.lookup_error)
        self.assertEqual(self.s.encode(self.encoding,
