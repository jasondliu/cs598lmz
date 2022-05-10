import codecs
# Test codecs.register_error - Issue #2633

class Codec(codecs.Codec):
    pass

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

def getregentry(encoding):
    if codecs.codec_search_function:
        encoding_name = codecs.codec_search_function(encoding)
    else:
        encoding_name = encoding

    return codecs.codec_map.get(encoding_name, None)

