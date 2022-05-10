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

class Test_UTF8_Bytes(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_utf8_bytes(self):
        import codecs
        enc = codecs.getencoder("utf-8")
        u = '\uDC80'
        self.assertRaises(UnicodeEncodeError, enc, u, "strict")

        class Abort(Exception): pass

        def f(exc):
            raise Abort

        codecs.register_error("abort", f)
        self.assertRaises(Abort, enc, u, "abort")

        enc = codecs.getencoder("utf-8")
        res = enc(u, "ignore")
        assert res == (b'', 1)

        res = enc(u, "replace")
        assert res == (b'?', 1)

        res = enc(u, "backslashreplace")
        assert res == (b'\\udc80', 1)

        getdec = codecs.get
