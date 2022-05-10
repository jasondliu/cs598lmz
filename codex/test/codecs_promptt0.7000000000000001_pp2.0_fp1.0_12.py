import codecs
# Test codecs.register_error
codecs.register_error('ignore', lambda x, y: ('', y + 1))

# Test Codec.encode()
def enc_ignore(exc):
    if isinstance(exc, UnicodeEncodeError):
        exc = UnicodeDecodeError(exc.encoding, exc.object, exc.start,
                                 exc.end, '?'*(exc.end-exc.start))
    raise exc

def enc_replace(exc):
    if isinstance(exc, UnicodeEncodeError):
        exc = UnicodeDecodeError(exc.encoding, exc.object, exc.start,
                                 exc.end, '?'*(exc.end-exc.start))
    raise exc

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)

