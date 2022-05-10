import codecs
# Test codecs.register_error()
class Codec_S1(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)

class Codec_S2(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table2)
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table2)

class StreamWriter_S1(Codec_S1,codecs.StreamWriter):
    pass

class StreamReader_S1(Codec_S1,codecs.StreamReader):
    pass

class StreamWriter_S2(Codec_S2,codecs.StreamWriter):
    pass

