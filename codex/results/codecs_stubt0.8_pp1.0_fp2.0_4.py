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

class TestUTF32(unittest.TestCase):
    def test_utf32_ascii(self):
        for dec, enc in (('utf-32', 'utf-32-le'), ('utf-32-le', 'utf-32'),
                         ('utf-32', 'utf-32-be'), ('utf-32-be', 'utf-32'),
                         ('utf-32', 'utf-32-ex'), ('utf-32-ex', 'utf-32'),
                         ('utf-32-le', 'utf-32-be'),
                         ('utf-32-le', 'utf-32-ex'),
                         ('utf-32-ex', 'utf-32-be'),
                         ('utf-32-be', 'utf-32-ex'),
                         ('utf-32-le', 'utf-32-le-ex'),
                         ('utf-32-be', 'utf-32-be-ex'),
                         ):
            u = "abc"
            for errors in "strict", "ignore", "replace":
                self.assertEqual(u.encode(enc, errors),

