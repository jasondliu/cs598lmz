import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test(unittest.TestCase):

    def test_utf8(self):
        self.assertEqual(
            codecs.decode('\x80', 'utf-8', 'strict'),
            '\x80'
        )
        self.assertEqual(
            codecs.decode('\x80', 'utf-8', 'ignore'),
            ''
        )
        self.assertEqual(
            codecs.decode('\x80', 'utf-8', 'replace'),
            '\ufffd'
        )

    def test_utf16(self):
        self.assertEqual(
            codecs.decode('\x80', 'utf-16', 'strict'),
            '\x80'
        )
        self.assertEqual(
            codecs.decode('\x80', 'utf-16', 'ignore'),
            ''
        )
        self.assertEqual(
            codecs.decode('\x80', 'utf-16
