import codecs
# Test codecs.register_error with 'replace' and 'xmlcharrefreplace'
# and a custom unencodable character handler.

class MyReplace(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)

def last_char(exc):
    if isinstance(exc, UnicodeEncodeError):
        return ord(exc.object[exc.start])
    else:
        return ord(exc.object[exc.start:exc.end][-1])

def cust_handler(exc):
    if isinstance(exc, UnicodeEncodeError):
        x = unichr(last_char(exc) + 1)
        return (x, exc.start + 1)
    else:
        x = unichr(last_char(exc) - 1)
        return (x, exc.end)

def test(
