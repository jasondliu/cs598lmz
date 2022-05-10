import codecs
# Test codecs.register_error
class Codec(codecs.Codec):
    def encode(self, input, errors="strict"):
        print "encoding %r with %r" % (input, errors)
        return codecs.charmap_encode(input, errors, encoding_table)
    def decode(self, input, errors="strict"):
        print "decoding %r with %r" % (input, errors)
        return codecs.charmap_decode(input, errors, decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, fi
