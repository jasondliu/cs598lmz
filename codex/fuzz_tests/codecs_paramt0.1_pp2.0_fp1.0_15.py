import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test_codecs(unittest.TestCase):

    def test_bug_4489(self):
        # Test for bug 4489:  codecs.open() should not swallow
        # LookupError exceptions
        self.assertRaises(LookupError, codecs.open,
                          os.path.join(os.path.dirname(__file__),
                                       "test_codecs_data", "test_4489"),
                          encoding="__spam__")

    def test_bug_4564(self):
        # Test for bug 4564:  codecs.open() should not swallow
        # AttributeError exceptions
        self.assertRaises(AttributeError, codecs.open,
                          os.path.join(os.path.dirname(__file__),
                                       "test_codecs_data", "test_4564"),
                          encoding="__spam__")

    def test_bug_4618(self):
        # Test for bug 4618:
