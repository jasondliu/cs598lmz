import codecs
# Test codecs.register_error
#
# This function is not used by the standard library, so it is tested
# here, instead of the test package.

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, {ord(u'\u3042'): 'A'})
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, 'A')

def encode(input, errors='strict'):
    return codecs.charmap_encode(input, errors, {ord(u'\u3042'): 'A'})

def decode(input, errors='strict'):
    return codecs.charmap_decode(input, errors, 'A')

