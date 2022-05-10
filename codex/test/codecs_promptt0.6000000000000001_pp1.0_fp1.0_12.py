import codecs
# Test codecs.register_error
class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return input, len(input)
    def decode(self, input, errors='strict'):
        return input, len(input)
def test_main():
    codecs.register(Codec)
    import test.test_codecs
    test.test_codecs.test_main()

