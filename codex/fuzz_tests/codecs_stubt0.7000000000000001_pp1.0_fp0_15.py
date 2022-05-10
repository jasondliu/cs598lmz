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

codecs.register_error("test_pmap_handler", pmap_error_handler)

class TestPmap(unittest.TestCase):
    def test_pmap_handler_utf8(self):
        self.assertEqual(pmap_error_handler(
                codecs.lookup_error("test_pmap_handler"), b'\xe6\x9c\xac\xe3\x81\x8b\x82\xcc\x83\x8a'),
                         (b'\xe6\x9c\xac\xe3\x81\x8b\x82\xcc\x83\x8a', 3))

    def test_pmap_handler_utf16(self):
        self.assertEqual(pmap_error_handler(
                codecs.lookup_error("test_pmap_handler"), b'\xd8\x3d\xde\x6d\xd8\x3d\xdc\xba\xd8\x3d\xdf\x9a'),
                        
