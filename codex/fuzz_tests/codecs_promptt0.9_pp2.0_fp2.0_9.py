import codecs
# Test codecs.register_error

class CodecException(Exception):
    codec_state = 0

    def __init__(self, state):
        self.codec_state = state

    def __str__(self):
        return 'CodecException: codec_state=%r' % self.codec_state

    __repr__ = __str__


class Codec(Codec, codecs.Codec):

    errors = 'strict'

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, {ch: u'\ufffd'[0]
            for ch in range(256)})

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, {0: u'\u1234'})


def codec_state_error_handler(error):
    if isinstance(error, CodecException):
        new_exc = error
    else:
        new_exc = CodecException(0)
        new_exc.end = error.end
       
