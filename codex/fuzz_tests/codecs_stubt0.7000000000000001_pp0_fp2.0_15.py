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

class ByteBuffer(object):
    def __init__(self):
        self.buf = []

    def write(self, s):
        self.buf.append(s)

    def getvalue(self):
        return b''.join(self.buf)

class TestDecode(unittest.TestCase):
    def assertDecode(self, enc, data, expected, **kwargs):
        actual = codecs.decode(data, enc, **kwargs)
        self.assertEqual(actual, expected)

    def test_error_handling(self):
        self.assertDecode("utf-8", b"\xff", "�")
        self.assertDecode("utf-8", b"\xff", "�", errors="ignore")
        self.assertDecode("utf-8", b"\xff", "")
        self.assertDecode("utf-8", b"\xff", "", errors="ignore")
        self.assertDecode("utf-8", b"\xff", "�", errors="replace")
        self.assertDecode("
