import codecs
# Test codecs.register_error
class Codec(codecs.Codec):
    def encode(self, input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_error_registry)
    def decode(self, input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_error_registry)
class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,self.errors,encoding_error_registry)[0]
class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input,self.errors,decoding_error_registry)[0]
class StreamWriter(Codec,codecs.StreamWriter):
    pass
class StreamReader(Codec,codecs.StreamReader):
    pass
### encodings module API
