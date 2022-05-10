import codecs
# Test codecs.register_error()

import codecs

class SurrogateTest(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(codecs.utf_7_decode('+AEI- +AOQ- +A-', 'surrogatepass'),
                         ('\u00e4\u00f6\u00fc', 13))
        self.assertEqual(codecs.utf_7_decode('+AEI- +AOQ- +A-', 'surrogateescape'),
                         ('\udce4\udcf6\udcfc', 13))
        self.assertEqual(codecs.utf_7_decode('+AEI- +AOQ- +A-', 'replace'),
                         ('\ufffd\ufffd\ufffd', 13))

    def test_encode(self):
        self.assertEqual(codecs.utf_7_encode('\u00e4\u00f6\u00fc', 'surrogateescape'),
                         ('+AEI- +AO
