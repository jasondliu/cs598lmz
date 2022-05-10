import codecs
# Test codecs.register_error

def bad_decode(input, errors='strict'):
    raise UnicodeError("bad error handler")

def bad_encode(input, errors='strict'):
    raise UnicodeError("bad error handler")

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

def getregentry():
    return (Codec().encode,Codec().decode,StreamReader,StreamWriter)

