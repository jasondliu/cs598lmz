import codecs
# Test codecs.register_error
# Written by Marc-Andre Lemburg (mal@lemburg.com).
import codecs

def force_unicode(s):
    return s.decode('ascii')

def search_function(encoding):
    if encoding != 'test.register_error':
        return None
    return codecs.CodecInfo(
        name='test.register_error',
        encode=force_unicode,
        decode=force_unicode,
        incrementalencoder=None,
        incrementaldecoder=None,
        streamreader=None,
        streamwriter=None,
        )

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        print 'decoding:', repr(input), final
        return codecs.charmap_decode(input, self.errors, decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        print 'encoding:', repr(input), final
        return codec
