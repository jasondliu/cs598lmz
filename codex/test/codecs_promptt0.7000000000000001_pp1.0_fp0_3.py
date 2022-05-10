import codecs
# Test codecs.register_error

def codec_error(errname):
    class Codec(codecs.Codec):
        def encode(self, input, errors='strict'):
            raise ValueError
        def decode(self, input, errors='strict'):
            raise ValueError
    class IncrementalEncoder(codecs.IncrementalEncoder):
        def encode(self, input, final=False):
            raise ValueError
    class IncrementalDecoder(codecs.IncrementalDecoder):
        def decode(self, input, final=False):
            raise ValueError
    class StreamWriter(Codec,codecs.StreamWriter):
        pass
    class StreamReader(Codec,codecs.StreamReader):
        pass
    if errname is None:
        return Codec
    else:
        return str(errname), Codec, (IncrementalEncoder, IncrementalDecoder, StreamReader, StreamWriter)

