import codecs
# Test codecs.register_error with 'xmlcharrefreplace'

class Codec(codecs.Codec):
    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_map)
    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_map)

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update({
    0x0080: 0x20ac,     # EURO SIGN
    0x0081: 0x0000,     # UNDEFINED
    0x0082: 0x201a,     # SINGLE LOW-9 QUOTATION MARK
    0x0083: 0x0192,     # LATIN SMALL LETTER F WITH HOOK
    0x0084: 0x201e,    
