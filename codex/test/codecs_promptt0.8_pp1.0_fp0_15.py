import codecs
# Test codecs.register_error

class CodecTestError(Exception):
    pass

class ErrorTest(codecs.Codec):
    def encode(self, input, errors='strict'):
        raise CodecTestError("encode error message")
    def decode(self, input, errors='strict'):
        raise CodecTestError("decode error message")

def search_function(encoding):
    if encoding == 'test.error':
        return Codec().encode,Codec().decode,StreamWriter().incrementalencoder,StreamReader().incrementaldecoder

codecs.register_error('test.error', lambda x: 'test.error')

codecs.lookup_error('test.error')

