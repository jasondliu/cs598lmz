import codecs
# Test codecs.register_error by encoding the start of the Hebrew alphabet
hebrew_string = "אבג"

print("Default behavior:")
print(hebrew_string.encode("ascii", "strict"))
print("Correct encoding:")
print(hebrew_string.encode("utf8"))
print("Forced encoding:")
codecs.register_error("strict", lambda e: ("?", e.start + 1))
print(hebrew_string.encode("ascii", "strict"))
 
class Codec(codecs.Codec):
    repr_errors = 'replace'

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(
