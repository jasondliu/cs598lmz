import codecs
# Test codecs.register_error
#
# By defining a new error handling function, we can trigger the error
# handling mechanism with arbitrary exceptions.

import codecs

X = 'x'

def search_function(encoding):
    if encoding == 'test.searchfunction.1':
        return codecs.charmap_encode
    elif encoding == 'test.searchfunction.2':
        return codecs.charmap_encode

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):
        return (X*len(input), len(input))

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return X*len(input)

    def reset(self):
        pass

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return X*len(input)

    def reset(self):
        pass

class StreamWriter(Codec,codecs.StreamWriter):
   
