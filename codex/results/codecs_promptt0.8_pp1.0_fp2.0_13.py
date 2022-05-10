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

decoding_table = (
    u'\x00'     #  0x00 -> NULL
    u'\x01'     #  0x01 -> START OF HEADING
    u'\x02'     #  0x02 -> START OF TEXT
    u'\x03'     #  0x03 -> END OF TEXT
    u'\x
