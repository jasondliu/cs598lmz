import codecs
# Test codecs.register_error
import _codecs
_codecs.register_error("test", codecs.replace_errors)
import binascii
def hex_codec(encoding):
    assert encoding == 'hex'
    encoder = codecs.getencoder('hex')
    decoder = codecs.getdecoder('hex')
    def encode(input, errors='strict'):
        return encoder(input, errors)
    def decode(input, errors='strict'):
        return decoder(input, errors)
    return encode, decode, None
codecs.register(hex_codec)
# test the various Unicode escape formats
# XXX only check strict mode
s = eval("""u'\\u0002\\U00000002\\N{STAR}\\N{star}\\N{star}\\u00a2'""")
# escape chars
for mod in "", "\\":
    # escape chars + hex chars
    for x in "0123456789abcdefABCDEF":
        for y in "0123456789abcdefABCDEF":
            v = '\\
