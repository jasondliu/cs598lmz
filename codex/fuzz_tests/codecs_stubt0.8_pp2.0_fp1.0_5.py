import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

class CodecsModuleTest(unittest.TestCase):

    def test_open_latin1(self):
        f = io.open("Modules/codecsdata/test_latin1.txt", "r",
                            encoding="latin1")
        self.assertEqual("\xff", f.read(1))

    def test_search_function(self):
        self.assertEqual("ascii",
                         codecs.lookup("ascii").name)
        self.assertEqual("charmap",
                         codecs.lookup("charmap").name)

    def test_system_errors(self):
        # Issue #4470
        with self.assertRaises(UnicodeDecodeError) as cm:
            codecs.charmap_decode("foo", "strict", "\x81")
        self.assertEqual(cm.exception.encoding, "charmap")
        self.assertEqual(cm.exception.object, "\x81")
        self.assertEqual(cm.exception
