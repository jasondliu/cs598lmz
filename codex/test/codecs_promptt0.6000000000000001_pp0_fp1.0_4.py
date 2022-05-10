import codecs
# Test codecs.register_error()

def search_function(encoding):
    if encoding != "test.unicode":
        return None
    def encode(input, errors="strict"):
        return (input.encode("utf-8"), len(input))
    def decode(input, errors="strict"):
        return (input.decode("utf-8"), len(input))
    return codecs.CodecInfo(encode, decode, name="test.unicode")

codecs.register(search_function)
