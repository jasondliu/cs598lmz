import codecs
# Test codecs.register_error()

import codecs

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)

def getregentry():
    return codecs.CodecInfo(name='cp1250',
                            encode=Codec().encode,
                            decode=Codec().decode,
                            incrementalencoder=None,
                            incrementaldecoder=None,
                            streamreader=None,
                            streamwriter=None)

