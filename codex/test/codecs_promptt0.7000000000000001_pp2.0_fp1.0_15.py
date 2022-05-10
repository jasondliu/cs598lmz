import codecs
# Test codecs.register_error

def search_function(encoding):
    if encoding=='test.searchfunction':
        import search_function
        return search_function.getregentry()
    return None

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,self.errors,encoding_map)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input,self.errors,decoding_map)[0]

