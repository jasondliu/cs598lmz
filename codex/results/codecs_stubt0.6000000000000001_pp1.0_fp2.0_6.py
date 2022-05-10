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


class TestUnicode(unittest.TestCase):

    def test_concatenation(self):
        # Concatenation
        self.assertEqual('a' + 'b', 'ab')
        self.assertEqual('a' + 'b' + 'c', 'abc')
        self.assertEqual('' + 'a', 'a')
        self.assertEqual('a' + '', 'a')
        self.assertEqual('abc' + 'def', 'abcdef')
        self.assertEqual('abc' + 'def' + 'ghi', 'abcdefghi')
        self.assertEqual('a' * 10, 'aaaaaaaaaa')
        self.assertEqual('a' * 10 + 'b', 'aaaaaaaaaab')
        self.assertEqual('a' * 10 + 'b' * 10, 'aaaaaaaaaabbbbbbbbbb')
        self.assertEqual('a' * 10 + 'bc' * 10, 'aaaaaaaaaabbcbcbcbcbcbcbcbcbcbcbcbcbc')

