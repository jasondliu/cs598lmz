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

utf8_test_string = "\U00010000\U00010001\U00010002\U00010003\U00010004\U00010005\U00010006\U00010007\U00010008\U00010009\U0001000a\U0001000b\U0001000c\U0001000d\U0001000e\U0001000f\U00010010"

class MyTest(unittest.TestCase):
    def test_utf8_stream_reader(self):
        for enc, text, ok in [("utf8", utf8_test_string, True),
                              ("utf8", "\xFF", False),
                              ("utf8", "\xFF\xFF", False),
                              ("utf8", "\xFF\xFF\xFF", False),
                              ("utf8", "\xFF\xFF\xFF\xFF", False),
                              ("utf8", "\xFF\xFF\xFF\xFF\xFF", False)]:
            #print("Text is", text)

            if ok:
               
