import codecs
# Test codecs.register_error

import codecs

def test(name):
    print name, ":"
    try:
        codecs.lookup_error(name)
    except LookupError:
        print "  not found"
    else:
        print "  found"

test("test")
codecs.register_error("test", lambda x: (u"\ufffd", x.start + 1))
test("test")

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)

class StreamWriter(Codec, codecs.StreamWriter):
    pass

class StreamReader(Codec, codecs.StreamReader):
    pass

def search_function(encoding):
    if encoding == 'test':
        return codecs.CodecInfo(
            name='test',
           
