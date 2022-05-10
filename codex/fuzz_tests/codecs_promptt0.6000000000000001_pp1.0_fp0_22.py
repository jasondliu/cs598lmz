import codecs
# Test codecs.register_error()

import codecs

def a_codec_name_function(name):
    if name == 'test.a':
        return codecs.lookup('ascii')
    return None

codecs.register(a_codec_name_function)

assert codecs.lookup('test.a').name == 'ascii'

try:
    codecs.lookup('bogus.name')
except LookupError:
    pass
else:
    print('LookupError expected')

# Application of codecs.lookup()

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.ch
