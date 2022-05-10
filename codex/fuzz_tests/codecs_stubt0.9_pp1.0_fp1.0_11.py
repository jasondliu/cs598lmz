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

from test import mapping_tests

class SurrogateMappingTest(mapping_tests.BasicTestMappingProtocol):
    inbase = '\ud800\ud801\ud802\ud803\udc00\udc01'
    outbase = 'abcde'
    indata = [unichr(ord(c)) for c in inbase]
    outdata = [ord(c) for c in outbase]
    resdata = dict(list(zip(indata, outdata)))
    pass


class SymmetricCodecTest(CodecsTestBase):
    def test_decode_with_errors(self):
        data = u"\udc00\uD800"
        a = data.encode("utf-16-le", "replace")
        b, c = a.decode("utf-16-le", "replace").split("?")
        self.assertEqual(b+c, "\udc00?\uD800")
        d = a.decode("utf-16-le", "ignore")
        self.assertE
