import codecs
# Test codecs.register_error():
class CodecRegError(codecs.Codec):

    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_map)

    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_map)

class CodecRegError_StreamWriter(CodecRegError,codecs.StreamWriter):
    pass

class CodecRegError_StreamReader(CodecRegError,codecs.StreamReader):
    pass

