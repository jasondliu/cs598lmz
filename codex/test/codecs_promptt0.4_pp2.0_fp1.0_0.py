import codecs
# Test codecs.register_error
# The error handler should be called with the following arguments:
# - exception object
# - encoding name
# - string being decoded
# - start position in the string
# - end position in the string
# - reason
# It should return a (replacement, new position) tuple.

import codecs
import sys

class Codec(codecs.Codec):
    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_map)
    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_map)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,self.errors,encoding_map)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_
