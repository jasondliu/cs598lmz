import codecs
# Test codecs.register_error("strict", codecs.strict_errors)
# Test codecs.register_error("ignore", codecs.ignore_errors)
# Test codecs.register_error("replace", codecs.replace_errors)

# The error handlers are registered under the name "test"
codecs.register_error("test", codecs.strict_errors)
codecs.register_error("test", codecs.ignore_errors)
codecs.register_error("test", codecs.replace_errors)

class Test_Codecs(unittest.TestCase):
    def test_builtin_lookup(self):
        self.assertEqual(codecs.lookup("ascii"), (codecs.ascii_decode,
                                                  codecs.ascii_encode,
                                                  None, None))
        self.assertEqual(codecs.lookup("mbcs"), (codecs.mbcs_decode,
                                                 codecs.mbcs_encode,
                                                 None, None))
        self.
