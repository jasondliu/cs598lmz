import codecs
# Test codecs.register_error.
#
# Note that the test depends on the base error handler being set to 'strict'
# prior to calling codecs.register_error, since codecs.register_error doesn't
# actually set the error handler to 'strict' if it is set to something else.
# See test_unicodeerrors for more exhaustive testing of error handlers.

encoding, data = 'utf-16', '\udc80xxxx'

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):

