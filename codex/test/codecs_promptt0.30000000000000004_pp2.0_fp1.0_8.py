import codecs
# Test codecs.register_error()

import codecs

def handler(exc):
    return (u'', exc.end)

codecs.register_error('test.my_error', handler)

class MyIncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        if final:
            raise UnicodeEncodeError("my_error", u"", 0, 1, "ouch")
        else:
            return input, len(input)

class MyIncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        if final:
            raise UnicodeDecodeError("my_error", "", 0, 1, "ouch")
        else:
            return input, len(input)

class MyStreamReader(codecs.StreamReader):
    def decode(self, input, errors='strict'):
        if errors != 'test.my_error':
            raise UnicodeDecodeError("my_error", "", 0, 1, "ouch")
