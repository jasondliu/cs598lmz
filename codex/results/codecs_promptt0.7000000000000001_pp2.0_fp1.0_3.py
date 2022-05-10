import codecs
# Test codecs.register_error for a case where the error handler
# gets called with a single argument

def results(obj):
    return [x for x in obj]

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors,
                                     {0x00: 'z', 0x01: 'a'})
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors,
                                     {'z': 0x00, 'a': 0x01})

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors,
                                     {0x00: 'z', 0x01: 'a'})[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap
