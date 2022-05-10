import codecs
# Test codecs.register_error()

class Codec(codecs.Codec):
    __qualname__ = 'Codec'
    encoding_map = codecs.make_encoding_map(u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, self.encoding_map)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, self.encoding_map)


class IncrementalEncoder(codecs.IncrementalEncoder):
    __qualname__ = 'IncrementalEncoder'

    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, Codec.encoding_map)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    __qualname__ = 'IncrementalDecoder
