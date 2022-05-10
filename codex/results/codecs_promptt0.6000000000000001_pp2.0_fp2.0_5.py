import codecs
# Test codecs.register_error

# code_page = 'cp932'
code_page = 'shift_jis'

def register_error(exc):
    print('register_error:', exc)
    return (u'', exc.start + 1)

codecs.register_error('test.errorhandler', register_error)

# codecs.lookup_error('test.errorhandler')

def encode(input, errors='strict'):
    return codecs.charmap_encode(input, errors, encoding_table)

def decode(input, errors='strict'):
    return codecs.charmap_decode(input, errors, decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_dec
