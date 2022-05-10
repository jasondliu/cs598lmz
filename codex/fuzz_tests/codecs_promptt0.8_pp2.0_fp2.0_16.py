import codecs
# Test codecs.register_error.
codecs.register_error('bad_error', lambda obj: (u'', obj.start + 1))

class TestCodec(unittest.TestCase):
    def assertEqualX(self, a, b):
        # Compares strings as if they were native strings
        self.assertEqual(a.encode(), b)

    def test_utf8(self):
        self.assertEqualX(codecs.utf_8_decode('\xc3\xa9\n')[0], '\xe9\n')
        self.assertEqualX(codecs.utf_8_encode('\xe9\n')[0], '\xc3\xa9\n')
        self.assertEqualX(codecs.utf_8_decode('\xc3\x28\n')[0], '\ufffd(\\n)')
        self.assertEqualX(codecs.utf_8_decode('\xc3\x28\n', 'replace')[0], '\uFFFD(\\n)
