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

class B1(Exception):
    pass

class B2(Exception):
    pass

b1 = B1()
b2 = B2()

def replace_b1(exc):
    if exc is b1:
        return "c"
    else:
        raise TypeError

def replace_b2(exc):
    if exc is b2:
        return "d"
    else:
        raise TypeError

codecs.register_error("replace_b1", replace_b1)
codecs.register_error("replace_b2", replace_b2)

class Incremental(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)

class Stream(codecs.StreamWriter):
    def __init__(self, errors="strict"):
        self.encoder = codecs.charmap_encode(errors, encoding_table)
    def reset(self):
        codecs.
