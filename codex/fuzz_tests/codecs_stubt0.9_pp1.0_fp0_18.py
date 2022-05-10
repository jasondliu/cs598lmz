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


# bpo-35916: Test that we can encode to every encoding and also decode
# from every encoding. Open the file to check that readline() works
# with that encoding.
try:
    maxunicode = sys.maxunicode
except AttributeError:
    maxunicode = 0x10FFFF

class TestBigRange(unittest.TestCase):
    def test_bigrange_encode(self):
        encodings = codecs.encode("", "replace").decode("ascii").splitlines()[1:]
        for encoding in encodings:
            text = chr(0)
            for i in range(maxunicode+1):
                try:
                    text = chr(i) + text
                except ValueError:
                    pass
            try:
                _ = codecs.encode(text, encoding)
                with open(TESTFN, "wt", encoding=encoding) as fobj:
                    fobj.write(text)
            except Exception as e:
                self.fail(encoding + ": " + str(e
