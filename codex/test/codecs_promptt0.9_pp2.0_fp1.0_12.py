import codecs
# Test codecs.register_error: class
class Codec(codecs.Codec):
    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_map)
    def decode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,decoding_map)
codecs.register(Codec)
class StreamWriter(Codec,codecs.StreamWriter):
    pass
class StreamReader(Codec,codecs.StreamReader):
    pass
# Test codecs.register_error: function
def search_function(name):
    if name.endwith('_function'):
        return name+'_Factory'
codecs.register(search_function)
#codecs.__all__ -- list of tuples(encoding,codecinfo,streaminfo)
# UTF-8
'\N{GREEK CAPITAL LETTER OMEGA}'.encode('UTF-8')
'\N{GREEK CAPITAL LETTER OMEGA}'.encode
