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


class IncrementalEncoderTest(unittest.TestCase):

    def test_constructor(self):
        incrementalencoder = IncrementalEncoder()

    def test_incrementalencoder(self):
        utf16_be = codecs.getincrementalencoder('utf-16-be')()
        utf16_le = codecs.getincrementalencoder('utf-16-le')()
        utf16_ex = codecs.getincrementalencoder('utf-16-ex')()
        ucs2 = codecs.getincrementalencoder('ucs2')()
        mbcs = codecs.getincrementalencoder('mbcs')()
        iso2022jp = codecs.getincrementalencoder('iso2022-jp')()
        rot_13 = codecs.getincrementalencoder('rot-13')()
        hex_codec = codecs.getincrementalencoder('hex')()
        base64_codec = codecs.getincrementalencoder('base64')()

        tests = [
            (utf16_be
