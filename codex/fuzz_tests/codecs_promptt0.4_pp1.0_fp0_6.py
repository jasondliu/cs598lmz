import codecs
# Test codecs.register_error

import codecs
import sys

def search_function(encoding):
    if encoding == "test.searchfunction":
        return codecs.lookup("utf-8")
    return None

codecs.register(search_function)

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):
        return codecs.utf_8_encode(input,errors)
    def decode(self,input,errors='strict'):
        return codecs.utf_8_decode(input,errors)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.utf_8_encode(input,self.errors)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.utf_8_decode(input,self.errors)[0]

class StreamWriter(Codec,codecs.StreamWriter):
    pass
