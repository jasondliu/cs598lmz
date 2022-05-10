import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad_decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad_encode"

codecs.register_error("test.bad_decode", bad_decode)
codecs.register_error("test.bad_encode", bad_encode)

def test_decode(input, errors="strict"):
    return codecs.charmap_decode(input, errors, {0x65: u"\u1234"})

def test_encode(input, errors="strict"):
    return codecs.charmap_encode(input, errors, {ord(u"\u1234"): 0x65})

class Test_Codecs(unittest.TestCase):

    def test_decode(self):
        self.assertEqual(test_decode("\x65"), (u"\u1234", 1))
        self.
