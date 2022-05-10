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

# Issue 7298
class StrSub(str):
    def __getitem__(self, i):
        return 'x'

def str_sub(exc):
    return (StrSub('x'), exc.start)

codecs.register_error("str_sub", str_sub)

class UnicodeSub(str):
    def __getitem__(self, i):
        return 'x'

def unicode_sub(exc):
    return (UnicodeSub(u'x'), exc.start)

codecs.register_error("unicode_sub", unicode_sub)

# Issue 7555
class RecursiveRepr(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return repr(self.value)

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)
    def decode(self, input, errors='
