import codecs
# Test codecs.register_error('test', codecs.replace_errors)

# Test codecs.register_error('test', codecs.replace_errors)
class Codec(codecs.Codec):
    __qualname__ = 'Codec'
    encode = codecs.charmap_encode
    decode = codecs.charmap_decode

class IncrementalEncoder(codecs.IncrementalEncoder):
    __qualname__ = 'IncrementalEncoder'
    def __init__(self, error='strict'):
        self.error = error
        self.data = ''

    def encode(self, input, final=False):
        self.data = self.data + input
        if final:
            return codecs.charmap_encode(self.data, self.errors)[0]
        else:
            return ''

    def reset(self):
        self.data = ''

    def getstate(self):
        return self.data

    def setstate(self, state):
        self.data = state

class IncrementalDecoder(codecs.Incre
