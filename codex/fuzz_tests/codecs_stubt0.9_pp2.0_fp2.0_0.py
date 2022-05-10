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

class SimpleUTF:
    def __init__(self, encoding="ascii", decoding_errors="strict"):
        self.encoding = encoding
        self.decoding_errors = decoding_errors
        self.decodename = "utf8"
        self.encode_errors = "strict"
        self.decodedetect = None

    def decode(self, input, errors="strict"):
        output = input.decode(self.decodename, errors)
        return (output, len(input))

    def encode(self, input, errors="strict"):
        output = input.encode(self.encoding, errors)
        return (output, len(input))

def run_single_test(encoding, errors, test):
    from test import string_tests
    string_tests.run_single_test(encoding, UnicodeError, errors, test)

def test_main():
    # test particularly funny UTF8 decoding errors, pick one error handler and
    # run all tests in that handler.

    for encoding, error, test in
