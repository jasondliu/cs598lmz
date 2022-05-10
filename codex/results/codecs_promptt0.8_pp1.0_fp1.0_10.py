import codecs
# Test codecs.register_error
# test register_error, unregister_error

def encode(input, errors=None):
    return ("testencoder", len(input)), len(input)

def decode(input, errors=None):
    return ("testdecoder", len(input)), len(input)

def badencode(input, errors=None):
    raise Exception, "badencode"

def baddecode(input, errors=None):
    raise Exception, "baddecode"

class CodingState:
    def __init__(self, stream):
        self.stream = stream

    def encode(self, input, errors="strict"):
        return codecs.charmap_encode(input, errors, self.stream)

    def decode(self, input, errors="strict"):
        return codecs.charmap_decode(input, errors, self.stream)


class Test_register_error:
    def test_register_error(self):
        # register new error handler
        stream = CodingState([1, 2, 3, 4])
        codec
