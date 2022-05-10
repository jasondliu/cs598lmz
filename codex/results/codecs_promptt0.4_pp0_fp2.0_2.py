import codecs
# Test codecs.register_error

# This test is not exhaustive.
# See test_codecs for more codec tests.

import codecs

def search_function(encoding):
    if encoding != 'test.unicode':
        return None
    class Codec(codecs.Codec):
        def encode(self, input, errors='strict'):
            return codecs.charmap_encode(input, errors,
                                         {ord(u'\u3042'): 'A'})
        def decode(self, input, errors='strict'):
            return codecs.charmap_decode(input, errors,
                                         {ord('A'): u'\u3042'})
    class StreamWriter(Codec, codecs.StreamWriter):
        pass
    class StreamReader(Codec, codecs.StreamReader):
        pass
    return (Codec().encode, Codec().decode, StreamReader, StreamWriter)

codecs.register(search_function)

def test_register_error():
    # Test codecs.register_error
    import codec
