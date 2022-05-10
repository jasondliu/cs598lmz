import codecs
# Test codecs.register_error
class Codec(codecs.Codec):
    __qualname__ = 'Codec'
    encode = codecs.charmap_encode
    decode = codecs.charmap_decode
class IncrementalEncoder(codecs.IncrementalEncoder):
    __qualname__ = 'IncrementalEncoder'
class IncrementalDecoder(codecs.IncrementalDecoder):
    __qualname__ = 'IncrementalDecoder'
class StreamWriter(Codec, codecs.StreamWriter):
    __qualname__ = 'StreamWriter'
class StreamReader(Codec, codecs.StreamReader):
    __qualname__ = 'StreamReader'
def getregentry():
    return codecs.CodecInfo(name='undefined', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)
codecs.register(getregentry)

class Test_register_error(unittest.TestCase):
    __qual
