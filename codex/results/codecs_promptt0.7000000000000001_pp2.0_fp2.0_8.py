import codecs
# Test codecs.register_error function
import codecs
import string

def search_function(encoding):
    if encoding != 'test.searchfunction': return None
    codec = codecs.codecs.lookup('utf-8')
    class IncrementalEncoder(codec.incrementalencoder):
        def encode(self, input, final=False):
            return codecs.utf_8_encode(input, self.errors)[0]
    class IncrementalDecoder(codec.incrementaldecoder):
        def decode(self, input, final=False):
            return codecs.utf_8_decode(input, self.errors)[0]
    class StreamWriter(codec.streamwriter):
        pass
    class StreamReader(codec.streamreader):
        pass
    return codecs.CodecInfo(
        name='test.searchfunction',
        encode=codec.encode,
        decode=codec.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=
