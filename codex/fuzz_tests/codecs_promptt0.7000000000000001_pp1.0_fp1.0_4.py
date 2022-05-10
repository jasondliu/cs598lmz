import codecs
# Test codecs.register_error
# Verify that the sys.stderr.encoding is 'ascii'
class Test_register_error(unittest.TestCase):
    def test_register_error(self):
        import codecs
        import sys
        self.assertEqual(sys.stderr.encoding, 'ascii')
        import codecs
        codecs.register_error('strict', codecs.strict_errors)
        codecs.register_error('ignore', codecs.ignore_errors)
        codecs.register_error('replace', codecs.replace_errors)
        codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
        codecs.register_error('backslashreplace', codecs.backslashreplace_errors)


if __name__ == '__main__':
    # unittest.main()
    pass
