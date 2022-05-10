import codecs
# Test codecs.register_error()

class Codec(codecs.Codec):
    __qualname__ = 'Codec'

    @staticmethod
    def encode(input, errors='strict'):
        return Codec.encode(input, errors)


class IncrementalEncoder(codecs.IncrementalEncoder):
    __qualname__ = 'IncrementalEncoder'

    def __init__(self, errors='strict'):
        codecs.IncrementalEncoder.__init__(self, errors)

    def encode(self, input, final=False):
        return Codec.encode(input, self.errors)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    __qualname__ = 'IncrementalDecoder'

    def __init__(self, errors='strict'):
        codecs.IncrementalDecoder.__init__(self, errors)

    def decode(self, input, final=False):
        return Codec.decode(input, self.errors)[0]


