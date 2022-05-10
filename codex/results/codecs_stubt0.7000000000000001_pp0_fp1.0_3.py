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

class TestFormat(unittest.TestCase):
    def test_utf8(self):
        for n in [2, 3, 4, 5, 10, 20, 100, 1000]:
            for test in [self.test_utf8_fixed, self.test_utf8_variable]:
                test(n)

    def test_utf8_fixed(self, n=None):
        data = 'x' * n
        encoded = data.encode('utf-8')
        self.assertEqual('%10s' % data, ' ' * 10 + data)
        self.assertEqual('%10s' % encoded, ' ' * 10 + data)
        self.assertEqual('%10r' % data, ' ' * 10 + repr(data))
        self.assertEqual('%10r' % encoded, ' ' * 10 + repr(encoded))

    def test_utf8_variable(self, n=None):
        data = 'x' * n
        encoded = data.encode('utf-8')
        self.assertEqual('%*s
