import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

def get_data(filename):
    with codecs.open(filename, encoding='utf-8', errors='surrogate_escape') as f:
        return f.read()

def get_data_b(filename):
    with open(filename, 'rb') as f:
        return f.read()

class Test_read_data(unittest.TestCase):

    def test_read_data(self):
        # This file contains the following three lines:
        # La Pe\xf1a
        # La Pe\ufffd\ufffda
        # La Pe\ufffd\ufffd\ufffd\ufffda
        data = get_data('surrogatepass_data.txt')
        self.assertEqual(data, 'La Peña\nLa Pe��a\nLa Pe��ña\n')

    def test_bad_read_data(self):
        # This file contains the following three lines:
        # La Pe\xf1a
        # La Pe\ufffd\
