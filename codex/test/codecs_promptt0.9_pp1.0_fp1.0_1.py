import codecs
# Test codecs.register_error:

# Classes for testing codecs.register_error
class Codec_X_X1(codecs.Codec):
    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_table)
    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_table)

