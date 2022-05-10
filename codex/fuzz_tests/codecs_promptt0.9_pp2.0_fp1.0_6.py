import codecs
# Test codecs.register_error
decode_error = codecs.lookup_error('surrogateescape')
class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_map)
class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_map)
class StreamWriter(Codec, codecs.StreamWriter):
    pass
class StreamReader(Codec, codecs.StreamReader):
    pass
def getregentry():
    return codecs.CodecInfo(name='undefined', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)


codecs.register(getregentry)
