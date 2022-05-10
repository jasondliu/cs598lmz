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


def make_iterdecode_error(enc, s, err):
    try:
        codecs.iterdecode(s, enc)
        while False:
            yield -1
    except err.__class__ as e:
        yield e

class MyUnicodeDecodeError(UnicodeDecodeError):
    def __str__(self):
        return "a"

class MyUnicodeEncodeError(UnicodeEncodeError):
    def __str__(self):
        return "a"

class MyUnicodeTranslateError(UnicodeTranslateError):
    def __str__(self):
        return "a"

class CodecTest(unittest.TestCase):

    def test_error_callback(self):
        encodings = [(chr if PY2 else str)(i) for i in range(256)]
        encodings = ["cp%04d" % i for i in range(256)] + ["iso8859_%d" % i for i in range(1, 16)] + [
            "mac_
