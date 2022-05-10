import codecs
# Test codecs.register_error()

import encodings.utf_8

class Codec(codecs.Codec):
    def encode(self,input,errors='strict'):
        return codecs.utf_8_encode(input,errors)
    def decode(self,input,errors='strict'):
        return codecs.utf_8_decode(input,errors,True)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.utf_8_encode(input,self.errors)[0]

class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_8_decode

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

def getregentry():
    return codecs.CodecInfo(
        name='utf8-sig',
        encode=Codec().encode,
        decode=
