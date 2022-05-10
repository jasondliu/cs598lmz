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

class TestExceptionHandler(unittest.TestCase):
    def test_utf16_surrogatepass(self):
        u = chr(0xd800)
        self.assertEqual(u.encode("utf-16-be", "surrogatepass"), b'\x00\xd8')
        self.assertEqual(u.encode("utf-16-le", "surrogatepass"), b'\xd8\x00')
        self.assertEqual(u.encode("utf-16", "surrogatepass"), b'\x00\xd8')
        self.assertIsInstance(u.encode("utf-16", "surrogatepass"), bytes)
        u = '\U0010ffff'
        self.assertEqual(u.encode("utf-16-be", "surrogatepass"), b'\xd8\xff\xdf\xff')
        self.assertEqual(u.encode("utf-16-le", "surrogatepass"), b'\xff\xd8\xff\xdf')
        self.
