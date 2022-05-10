import codecs
# Test codecs.register_error
def encoder(encoding):
    def f(s):
        return s.replace('a', 'x').encode(encoding)
    return codecs.CodecInfo(name=encoding, encode=cencoders.encode, decode=cencoders.decode, incrementalencoder=None, incrementaldecoder=None, streamreader=None, streamwriter=None)

def decoder(encoding):
    def f(s):
        return s.decode(encoding).replace('x', 'a')
    return codecs.CodecInfo(name=encoding, encode=cencoders.encode, decode=cencoders.decode, incrementalencoder=None, incrementaldecoder=None, streamreader=None, streamwriter=None)

codecs.register(encoder)
codecs.register(decoder)
