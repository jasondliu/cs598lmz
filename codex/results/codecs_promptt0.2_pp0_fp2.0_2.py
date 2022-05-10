import codecs
# Test codecs.register_error

# This test is a bit of a hack, but it should work.

# First, we need a codec that raises an error.  We'll use the
# 'surrogateescape' error handler for this.

def encode(input, errors='surrogateescape'):
    return codecs.charmap_encode(input, errors, encoding_table)

def decode(input, errors='surrogateescape'):
    return codecs.charmap_decode(input, errors, decoding_table)

class Codec(codecs.Codec):
    def encode(self, input, errors='surrogateescape'):
        return codecs.charmap_encode(input, errors, encoding_table)
    def decode(self, input, errors='surrogateescape'):
        return codecs.charmap_decode(input, errors, decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self
