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

class BytesHandler:
    def __init__(self):
        self.errors = 0
        self.decoded_bytes = 0

    def write(self, bytes):
        self.decoded_bytes += len(bytes)

    def handle_error(self):
        self.errors += 1

# Test the 'replace' error handler.
def test_replace_handler(unicode_, utf8, utf8_with_errors, utf8_with_errors_and_surrogates, utf16_with_errors, utf32_with_errors):
    def test_text_decoder(decoder):
        decoder.decode(utf8_with_errors, "replace")
        assert decoder.errors == 2
        assert decoder.decoded_bytes == len(utf8_with_errors)

    def test_bytes_decoder(decoder):
        decoder.decode(utf8_with_errors, "replace")
        assert decoder.errors == 2
        assert decoder.decoded_bytes == len(utf8_with_errors
