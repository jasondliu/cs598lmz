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

class Test_codecs(unittest.TestCase):

    def test_readbuffer(self):
        # the buffer should be exactly what we wrote
        # create a buffer with some non-ascii
        b = bytes(bytearray(range(0x80, 0x100)))
        # write it to a BytesIO output file
        import io
        fp = io.BytesIO()
        fp.write(b)
        # create a TextIOWrapper around it with a utf8 decoder
        fp.seek(0)
        text = io.TextIOWrapper(fp, encoding="utf8")
        # read from the buffer
        self.assertEqual(text.read(), "�")
        # make sure we can read again
        self.assertEqual(text.read(), "")
        # make sure the buffer is exactly what we wrote
        fp.seek(0)
        self.assertEqual(fp.read(), b)

        # do the same thing with a non-empty buffer
        b = bytes(bytear
