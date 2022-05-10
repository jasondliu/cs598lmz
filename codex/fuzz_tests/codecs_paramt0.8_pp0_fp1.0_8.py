import codecs
codecs.register_error('restrict_ascii', restrict_ascii)

# Install the custom codec
codecs.register(search_function)

class Base64Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return (Base64.encodebytes(input), len(input))

    def decode(self, input, errors='strict'):
        return (Base64.decodebytes(input), len(input))

class Base64IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        assert self.errors == 'strict'
        return Base64.encodebytes(input)

class Base64IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        assert self.errors == 'strict'
        return Base64.decodebytes(input)

class Base64StreamReader(Base64IncrementalDecoder, codecs.StreamReader):
    pass

class Base64StreamWriter(Base64Incre
