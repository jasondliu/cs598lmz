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

class StatefulIncrementalEncoder(codecs.IncrementalEncoder):
    def __init__(self, errors="strict"):
        codecs.IncrementalEncoder.__init__(self, errors)
        self.reset()

    def reset(self):
        self.state = 0

    def encode(self, input, final=False):
        if self.state == 0:
            self.state = 1
            return codecs.charmap_encode(input, self.errors, encoding_table)[0]
        else:
            return codecs.charmap_encode(input, self.errors, step_table)[0]

class StatefulIncrementalDecoder(codecs.IncrementalDecoder):
    def __init__(self, errors="strict"):
        codecs.IncrementalDecoder.__init__(self, errors)
        self.reset()

    def reset(self):
        self.state = 0

    def decode(self, input, final=False):
        if self.state == 0:
            self.state =
