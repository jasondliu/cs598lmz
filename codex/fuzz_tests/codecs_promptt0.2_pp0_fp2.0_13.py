import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    return (u'', len(input))

def bad_encode(input, errors='strict'):
    return (u'', len(input))

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return bad_encode(input, errors)
    def decode(self, input, errors='strict'):
        return bad_decode(input, errors)

class StreamWriter(Codec, codecs.StreamWriter):
    pass

class StreamReader(Codec, codecs.StreamReader):
    pass

def search_function(encoding):
    if encoding == 'test.bad':
        return codecs.CodecInfo(
            name='test.bad',
            encode=bad_encode,
            decode=bad_decode,
            incrementalencoder=None,
            incrementaldecoder=None,
            streamreader=StreamReader,
            streamwriter=StreamWriter,
        )
   
