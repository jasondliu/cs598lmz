import codecs
# Test codecs.register_error()


class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return input + '-encode', len(input)

    def decode(self, input, errors='strict'):
        return input + '-decode', len(input)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        if final:
            return input + '-encode-final'
        return input + '-encode', len(input)


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        if final:
            return input + '-decode-final'
        return input + '-decode', len(input)


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def test(encoding):
    import StringIO
    import sys
    s = StringIO.StringIO
