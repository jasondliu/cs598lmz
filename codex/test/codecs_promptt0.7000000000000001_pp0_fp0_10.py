import codecs
# Test codecs.register_error
# Requires that the error handler be available as a global, so we can get at
# it for the test.
class Codec_S(codecs.Codec):
    def encode(self, input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_map)
    def decode(self, input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_map)

class Codec_Error(Exception):
    def __init__(self,encoding,reason):
        self.encoding = encoding
        self.reason = reason
    def __str__(self):
        return 'Codec_Error:%s' % self.reason

def codec_search_function(encoding):
    if encoding == 'test.unicode':
        return (Codec_S().encode,Codec_S().decode,None,None)
