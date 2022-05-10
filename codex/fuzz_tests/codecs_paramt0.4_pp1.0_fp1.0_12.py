import codecs
codecs.register_error('strict', codecs.ignore_errors)

def encode(input, errors='strict'):
    return (input.encode('utf-8', errors), len(input))

def decode(input, errors='strict'):
    return (input.decode('utf-8', errors), len(input))

class StreamReader(codecs.StreamReader):
    def decode(self, input, errors='strict'):
        return codecs.utf_8_decode(input, errors, True)

class StreamWriter(codecs.StreamWriter):
    def decode(self, input, errors='strict'):
        return codecs.utf_8_decode(input, errors, True)

def getregentry():
    return codecs.CodecInfo(
        name='utf-8-sig',
        encode=encode,
        decode=decode,
        incrementalencoder=codecs.IncrementalEncoder,
        incrementaldecoder=codecs.IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=Stream
