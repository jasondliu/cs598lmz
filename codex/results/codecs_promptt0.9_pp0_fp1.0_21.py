import codecs
# Test codecs.register_error
import codecs; sys.stdout = codecs.getwriter('utf-8')()
def encode(input, errors='strict'):
    return codecs.charmap_encode(input, errors, encoding_table)
def decode(input, errors='strict'):
    return codecs.charmap_decode(input, errors, decoding_table)
class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return encode(input, self.errors)[0]
class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return decode(input, self.errors)[0]
class StreamWriter(Codec,codecs.StreamWriter):
    pass
class StreamReader(Codec,codecs.StreamReader):
    pass
### encodings module API
def getregentry():
    return codecs.CodecInfo( name='mac_cyrillic',
                             encode=encode,
                             decode=decode,

