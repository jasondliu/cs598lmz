import codecs
# Test codecs.register_error()

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return input.replace('x', ''), len(input)
    def decode(self, input, errors='strict'):
        return input.replace('x', ''), len(input)

codecs.register(lambda name: Codec() if name == 'null' else None)

# Encoding and decoding tests
