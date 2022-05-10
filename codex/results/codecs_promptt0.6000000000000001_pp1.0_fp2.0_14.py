import codecs
# Test codecs.register_error with "bad" codecs

import codecs
import sys

# A "bad" codec that should never be used
def bad_encode(input, errors="strict"):
    raise UnicodeError("bad_encode: bad encoding")
def bad_decode(input, errors="strict"):
    raise UnicodeError("bad_decode: bad encoding")

class MyReplace(object):
    def __init__(self, old, new):
        self.old = old
        self.new = new
    def __call__(self, e):
        return (self.new, e.start + len(self.old))

def test(name, encode, decode, expected):
    for input in ["abc", u"abc"]:
        try:
            codecs.register_error(name, encode)
            codecs.register_error(name, decode)
            if input is unicode:
                s = input.encode(name)
            else:
                s = input.decode(name)
        except UnicodeError:
            s = None
        if s
