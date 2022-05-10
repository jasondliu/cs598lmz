import codecs
# Test codecs.register_error with unicode_internal

import codecs

class Decoder(codecs.BufferedIncrementalDecoder):

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input,errors,'strict')

def search_function(encoding):
    if encoding!='unicode_internal':
        return None
    return codecs.CodecInfo(
        name='unicode_internal',
        encode=codecs.charmap_encode,
        decode=Decoder,
    )

codecs.register(search_function)

s = 'ab\u0c31\u0c32cd'
