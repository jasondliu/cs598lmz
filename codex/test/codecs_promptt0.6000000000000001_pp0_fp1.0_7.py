import codecs
# Test codecs.register_error()
import re

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return re.sub('[\x80-\xff]', '?', input), len(input)
    def decode(self, input, errors='strict'):
        return re.sub('[\x80-\xff]', '?', input), len(input)

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

def getregentry():
    return codecs.CodecInfo(
        name='reject',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=None,
        incrementaldecoder=None,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )

codecs.register(getregentry)

### encodings module API

