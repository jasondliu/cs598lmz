import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

def get_data(filename):
    with open(filename, 'rb') as f:
        return f.read().decode('utf-8', 'surrogatepass')

class TestRSTXMLTranslator(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_basic(self):
        input = get_data('data/basic.rst')
        want = get_data('data/basic.xml')
        got = publish_string(source=input, writer=RSTXMLTranslator)
        self.assertMultiLineEqual(want, got)

    def test_unicode(self):
        input = get_data('data/unicode.rst')
        want = get_data('data/unicode.xml')
        got = publish_string(source=input, writer=RSTXMLTranslator)
        self.assertMultiLineEqual(want, got)

    def test_admonitions(self):
        input
