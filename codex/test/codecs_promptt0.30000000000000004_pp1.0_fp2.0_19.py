import codecs
# Test codecs.register_error()

# This test is based on the one in test_codecs.py, but uses the
# surrogateescape error handler.

import codecs
import unittest

class Test_SurrogateEscape(unittest.TestCase):
    def test_surrogateescape(self):
        # test the surrogateescape error handler
        for c in (0xd800, 0xdc00, 0xdfff):
            self.assertEqual(
                codecs.decode(bytes([c]), "ascii", "surrogateescape"),
                bytes([c])
            )
            self.assertEqual(
                codecs.decode(bytes([c]), "ascii", "surrogatepass"),
                bytes([c])
            )
            self.assertEqual(
                codecs.decode(bytes([c]), "ascii", "surrogateescape"),
                bytes([c])
            )
