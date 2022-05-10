import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

class EncodingMapTest(unittest.TestCase):

    def test_basemapping(self):

        class Codec(codecs.Codec):

            def encode(self, input, errors='strict'):
                return codecs.charmap_encode(input,errors,encoding_map)

            def decode(self, input, errors='strict'):
                return codecs.charmap_decode(input,errors,decoding_map)

        class StreamWriter(Codec, codecs.StreamWriter):
            pass

        class StreamReader(Codec, codecs.StreamReader):
            pass

        def search_function(encoding):
            if encoding == 'test_codec':
                return (Codec,StreamReader,StreamWriter)
            return None

        self.assertEqual(u'abc', codecs.decode(input, 'test_codec', 'strict'))
        self.assertEqual(u'abcdefghi', codecs.decode(input+input[:3], 'test_codec', 'strict'
