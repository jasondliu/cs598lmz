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

class CodecsModuleTest(unittest.TestCase):

    def test_utf7(self):
        utfTests = [
            ("\u20ac", "+AOQ-"),
            ("\uffff", "+/v8-"),
            ("abc\u20ac\u20ac\u20ac", "abc+AOQAOQAOQ-"),
            ("\u20ac\u20ac\u20acabc", "+AOQAOQAOQabc"),
            ("\u20ac\u20ac\u20ac", "+AOQAOQAOQ-"),
            ("+AOQAOQAOQ-", "+AOQAOQAOQ-"),
            ("+AOQAOQAOQabc", "+AOQAOQAOQabc"),
            ("+AOQAOQAOQ-def+ACEAIg-", "+AOQAOQAOQ-def+ACEAIg-"),
            ("+AOQAOQAOQ-
