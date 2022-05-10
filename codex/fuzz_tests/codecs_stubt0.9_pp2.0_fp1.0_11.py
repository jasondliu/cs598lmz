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

class RegErrorHandle(unittest.TestCase):

    def test_error_handlers(self):
        self.assertEqual("abc".encode("unicode-escape", "add_one_codepoint"), "ab\\ucf77c")
        self.assertEqual("abc".encode("utf-16", "add_utf16_bytes"), "abcdab".encode("utf-16"))
        self.assertEqual("abc".encode("utf-32", "add_utf32_bytes"), "abcdabcd".encode("utf-32"))

def test_main():
    run_unittest(RegErrorHandle)

if __name__ == '__main__':
    test_main()
