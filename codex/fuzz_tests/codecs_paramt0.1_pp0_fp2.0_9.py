import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test_codecs_ignore_errors(unittest.TestCase):

    def test_main(self):
        self.assertEqual(codecs.strict_errors(u'\ufffe'), (u'\ufffe', 1))
        self.assertEqual(codecs.strict_errors(u'\ufffe'), (u'\ufffe', 1))
        self.assertEqual(codecs.strict_errors(u'\ufffe'), (u'\ufffe', 1))
        self.assertEqual(codecs.strict_errors(u'\ufffe'), (u'\ufffe', 1))
        self.assertEqual(codecs.strict_errors(u'\ufffe'), (u'\ufffe', 1))
        self.assertEqual(codecs.strict_errors(u'\ufffe'), (u'\ufffe', 1))
        self.assertEqual(codecs.strict_errors(u'
