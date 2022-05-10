import codecs
# Test codecs.register_error()

# Bypass the special casing for ASCII
# in the codecs module.

import codecs
import encodings

def raise_error(ex):
    raise ex

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_map)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_map)[0]

class StreamWriter(codecs.StreamWriter):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)[0]

class StreamReader(codecs.StreamReader):
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)[0]

