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

class Test_StreamReaderWriter(unittest.TestCase):
    def test_readline(self):
        source = ["line 1\n", "line 2\n", "line 3\n"]
        target = "line 1\nline 2\nline 3\n"
        for buffering in 1, 2:
            for read1 in 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000:
                for read2 in 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000:
                    s = "buffering %d, read1 %d, read2 %d" % (buffering, read1, read2)
                    input = "".join(source)
                    r = codecs.getreader("utf-8")(StringIO.StringIO(input),
                                                  buffering=buffering)
                    output = ""
                    while True:
                        c = r.read1(read1)
                        if not c:
                            break
                        output += c
                        c =
