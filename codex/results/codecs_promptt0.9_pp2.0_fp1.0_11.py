import codecs
# Test codecs.register_error method
class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        if 'X' in input:
            raise UnicodeDecodeError("test", 'X',
                                     input.find('X'),
                                     input.find('X')+1,
                                     "test")
        return codecs.utf_8_encode(input, self.errors)[0]

class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_8_decode

class StreamWriter(codecs.StreamWriter):
    pass

class StreamReader(codecs.StreamReader):
    pass

### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name="test-encode-decode-error",
        encode=IncrementalEncoder,
        decode=IncrementalDecoder,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter
