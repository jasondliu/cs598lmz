import codecs
codecs.register_error('strict', codecs.ignore_errors)


class TestOptions(unittest.TestCase):

    def setUp(self):
        self.parser = optparse.OptionParser()

    def test_strict_unicode(self):
        self.parser.add_option('-d', '--default', action="store",
                               default=u"default\u2026")
        self.parser.add_option('-e', '--explicit', action="store",
                               type="string")
        options, args = self.parser.parse_args([])
        self.assertEqual(options.default, u"default\u2026")
        self.assertEqual(options.explicit, None)
        self.assertEqual(type(options.default), unicode)
        self.assertEqual(type(options.explicit), type(None))

    def test_unicode_explicit(self):
        self.parser.add_option('-d', '--default', action="store",
                               default=u"default\u2026")
        self
