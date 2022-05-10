import codecs
# Test codecs.register_error()

import codecs

def my_handler(exception):
    return (u'', exception.start + 1)

codecs.register_error('my_handler', my_handler)

def my_decoder(input, errors='strict'):
    return codecs.charmap_decode(input, errors, {'a': u'\u1234'})

def my_encoder(input, errors='strict'):
    return codecs.charmap_encode(input, errors, {u'\u1234': 'a'})

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return my_encoder(input, errors)
    def decode(self, input, errors='strict'):
        return my_decoder(input, errors)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return my_encoder(input, self.errors)[0]

