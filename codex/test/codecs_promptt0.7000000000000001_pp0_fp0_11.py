import codecs
# Test codecs.register_error and .strict

class Codec_S(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)

class Codec_S2(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map2)

class StreamWriter_S(Codec_S, codecs.StreamWriter):
    pass

class StreamReader_S(Codec_S, codecs.StreamReader):
    pass

class StreamReader_S2(Codec_S2, codecs.StreamReader):
    pass

