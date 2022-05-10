import codecs
# Test codecs.register_error

# Create a codec that incodes bytes as ints and decodes ints as bytes,
# also swapping bytes on the way in and out.  Use the "namereplace"
# error handler.  The character U+00FF will translate to the integer
# 255 and back to U+00FF.  Other characters will cause a UnicodeError
# with name 'namereplace' in the context of the test.

def my_encode(input, errors='strict'):
    return (list(input), len(input))

def my_decode(input, errors='strict'):
    return (bytes(reversed(input)), len(input))

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return my_encode(input, errors)
    def decode(self, input, errors='strict'):
        return my_decode(input, errors)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return my_encode(
