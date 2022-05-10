import codecs
# Test codecs.register_error()

import codecs
import sys

class Codec(codecs.Codec):
    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_map)
    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_map)

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

def getregentry():
    return codecs.CodecInfo(
        name='test_register_error',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=codecs.IncrementalEncoder,
        incrementaldecoder=codecs.IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    )

