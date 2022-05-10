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


class IncrementalUTF8Reader:

    def decode(self, input, errors='strict'):
        return codecs.utf_8_decode(input, errors)[0]


class IncrementalUTF16Reader:

    def decode(self, input, errors='strict'):
        return codecs.utf_16_decode(input, errors, True)[0]


class IncrementalUTF32Reader:

    def decode(self, input, errors='strict'):
        return codecs.utf_32_decode(input, errors, True)[0]


class IncrementalUTF16ReaderLE:

    def decode(self, input, errors='strict'):
        return codecs.utf_16_decode(input, errors, False)[0]


class IncrementalUTF32ReaderLE:

    def decode(self, input, errors='strict'):
        return codecs.utf_32_decode(input, errors, False)[0]

class IncrementalUTF16ReaderBE:

    def decode(self, input, errors='strict'):
        return codecs
