import codecs
# Test codecs.register_error

def lookup(name):
    if name == "test":
        return codecs.lookup_error("ignore")
    else:
        return None

codecs.register_error("test", lookup)

codecs.lookup_error("test")

# Test codecs.register

def search_function(encoding):
    if encoding == "test":
        class Codec:
            def encode(self, input, errors="strict"):
                return "".join(map(lambda x: chr(ord(x)+1), input)), len(input)
            def decode(self, input, errors="strict"):
                return "".join(map(lambda x: chr(ord(x)-1), input)), len(input)
            def getregentry(self):
                return None
        return (Codec().encode, Codec().decode, None, None)
    else:
        return None

codecs.register(search_function)

codecs.lookup("test")

# Test codecs.getencoder/decoder

