import codecs
# Test codecs.register_error:

# Classes for testing codecs.register_error
class Codec_X_X1(codecs.Codec):
    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_table)
    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_table)

class Codec_X_X1E(Codec_X_X1):
    def encode(self,input,errors='strict'):
        try:
            return Codec_X_X1.encode(input,errors)
        except UnicodeEncodeError,e:
            return encoding_error(e)

class Codec_X_X1D(Codec_X_X1):
    def decode(self,input,errors='strict'):
        try:
            return Codec_X_X1.decode(input,errors)
        except UnicodeDecodeError,e:
            return decoding_error(e)

# Functions
