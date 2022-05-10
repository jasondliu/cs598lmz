import codecs
# Test codecs.register_error

def bad_decode(input, errors='strict'):
    print('bad_decode(%r, %r)' % (input, errors))
    raise UnicodeDecodeError('unknown', input, 0, 1, 'ouch')

class bad_encode(codecs.Codec):
    def encode(self, input, errors='strict'):
        print('bad_encode.encode(%r, %r)' % (input, errors))
        raise UnicodeEncodeError('unknown', input, 0, 1, 'ouch')
    def decode(self, input, errors='strict'):
        print('bad_encode.decode(%r, %r)' % (input, errors))
        raise UnicodeDecodeError('unknown', input, 0, 1, 'ouch')

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

encoding = 'ascii'

print('Trying plain "strict" encoding')
try
