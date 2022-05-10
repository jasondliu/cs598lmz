import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == "test.searchfunction":
        return codecs.search_function("utf-8")
    else:
        return None

codecs.register(search_function)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.utf_8_encode(input, self.errors)[0]

class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_8_decode

class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_8_encode

class StreamReader(codecs.StreamReader):
    decode = codecs.utf_8_decode

### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name='test.searchfunction',
        encode=IncrementalEncoder,
        decode=IncrementalDecoder,
        incremental
