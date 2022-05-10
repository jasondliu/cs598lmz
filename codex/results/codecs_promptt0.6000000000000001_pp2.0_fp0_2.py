import codecs
# Test codecs.register_error('strict', codecs.replace_errors)
# codecs.register_error('strict', codecs.replace_errors)
# codecs.register_error('strict', codecs.strict_errors)
# codecs.register_error('strict', codecs.surrogate_or_strict)
# codecs.register_error('strict', codecs.surrogatepass_handler)
# codecs.register_error('strict', codecs.surrogatepass_or_strict)
# codecs.register_error('strict', codecs.xmlcharrefreplace_errors)
# codecs.register_error('strict', codecs.xmlcharrefreplace_handler)
# codecs.register_error('strict', codecs.xmlcharrefreplace_errors)


class TestCsv(unittest.TestCase):
    def setUp(self):
        self.test_file_path = os.path.join(os.path.dirname(__file__), 'test.csv')
        self.test_file_path_with_header =
