import codecs
# Test codecs.register_error()

import codecs
import encodings, encodings.utf_8
import re, sys

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def __init__(self, errors='strict'):
        codecs.IncrementalEncoder.__init__(self, errors)
    def encode(self, input, final=False):
        if final:
            return codecs.charmap_encode(input, self.errors, encoding_table)[0]
        else:
            return codecs.charmap_encode(input, self.errors, encoding_table)[0]

