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

class STREAMReaderTest(unittest.TestCase):

    def tearDown(self):
        if (sys.platform != "win32"):
            sys.stdin = sys.__stdin__

    def test_streamreader_translate(self):
        from io import BytesIO

        # The test should work for any kind of file objects
        for bufsize in (0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024):
            # Read from a file
            with open(support.TESTFN, "rb") as fp:
                stream = io.TextIOWrapper(fp, encoding="utf-16-le",
                                          newline="\n", line_buffering=False,
                                          buffering=bufsize)
                data = stream.read()
                self.assertEqual(data, support.TEST_STRING)
                self.assertEqual(stream.newlines, "\n")
                self.assertEqual(stream.read(), "")
                self.assertEqual(stream.tell
