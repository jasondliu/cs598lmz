import codecs
# Test codecs.register_error()

from test import test_support

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
        name='test-codec-register-error',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=None,
        incrementaldecoder=None,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )

encoding_map = codecs.make_encoding_map(range(256))
decoding_map = dict([(v, k) for k
