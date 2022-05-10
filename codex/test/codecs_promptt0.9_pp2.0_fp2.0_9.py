import codecs
# Test codecs.register_error

class CodecException(Exception):
    codec_state = 0

    def __init__(self, state):
        self.codec_state = state

    def __str__(self):
        return 'CodecException: codec_state=%r' % self.codec_state

    __repr__ = __str__


