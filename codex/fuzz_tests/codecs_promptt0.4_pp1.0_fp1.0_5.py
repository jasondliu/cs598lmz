import codecs
# Test codecs.register_error()

import codecs

def test(name):
    print 'Testing %s' % name
    try:
        codecs.lookup_error(name)
    except LookupError, e:
        print '  LookupError:', e
    else:
        print '  No LookupError'

test('test')

def handler(exception):
    print 'handler:', exception
    return (u'', exception.end)

codecs.register_error('test', handler)

test('test')

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,
