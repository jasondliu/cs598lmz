import codecs
# Test codecs.register_error()
import codecs

# This is a codec which encodes to upper-case and
# decodes to lower-case.

class Codec:
    def __init__(self):
        self.encoding = 'upper'

    def encode(self, input, errors='strict'):
        return input.upper(), len(input)

    def decode(self, input, errors='strict'):
        return input.lower(), len(input)

def test():
    # UnicodeDecodeError is raised by the buffered reader when it
    # encounters an invalid character
    text = 'abc\xFF\n'
    # Register the codec
    codecs.register(lambda name: codecs.lookup('upper') if name == 'upper' else None)
    # Read the text with the upper codec
    f = codecs.open('test.txt', 'r', 'upper')
