import codecs
# Test codecs.register_error
# bug: http://bugs.python.org/issue11479
# bug: http://bugs.python.org/issue11478
# bug: http://bugs.python.org/issue10755
# bug: http://bugs.python.org/issue12281
# bug: http://bugs.python.org/issue12533
# bug: http://bugs.python.org/issue12536
class CodecTests(unittest.TestCase):
    def test_register(self):
        # Bug #11479: "xmlcharrefreplace" error handler not working in codecs
        codecs.register_error("test_handler", codecs.xmlcharrefreplace_errors)
        self.assertTrue(codecs.lookup_error("test_handler") is
          codecs.xmlcharrefreplace_errors)
        codecs.register_error("test_handler", None)

    def test_register_lookup_unknown_handler(self):
        # Bug #11478: unknown error handler should raise LookupError, not
        # TypeError
        self.assertRaises(LookupError,
