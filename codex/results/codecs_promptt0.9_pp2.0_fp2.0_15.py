import codecs
# Test codecs.register_error()

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return input.replace('x', ''), len(input)
    def decode(self, input, errors='strict'):
        return input.replace('x', ''), len(input)

codecs.register(lambda name: Codec() if name == 'null' else None)

# Encoding and decoding tests
print('abc'.encode('null', 'backslashreplace'))
print(b'abc'.decode('null', 'backslashreplace'))

print('abc'.encode('null'))
print(b'abc'.decode('null'))

# Encoding map
print('xy'.encode('null'))

# Decoder map
print(b'xy'.decode('null'))
