import codecs
# Test codecs.register_error

import codecs

def bad_errorhandler(exception):
    raise TypeError("bad errorhandler")

def good_errorhandler(exception):
    return (u"\ufffd", exception.end)

def bad_decode(input, errors="strict"):
    return (u"\ufffd", 1)

def bad_encode(input, errors="strict"):
    raise UnicodeEncodeError("bad_encode", u"\u3042", 0, 1, "bad_encode")

class Codec(codecs.Codec):
    def encode(self, input, errors="strict"):
        return bad_encode(input, errors)
    def decode(self, input, errors="strict"):
        return bad_decode(input, errors)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return bad_encode(input, self.errors)[0]

