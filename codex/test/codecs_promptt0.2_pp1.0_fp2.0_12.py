import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError("bad decode")

def bad_encode(input, errors='strict'):
    raise UnicodeError("bad encode")

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_map)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_map)[0]

