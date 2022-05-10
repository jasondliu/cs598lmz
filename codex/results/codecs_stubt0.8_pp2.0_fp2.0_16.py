import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)
# Note that that register_error makes a call to _PyCodec_LookupError
# which may call codecs.encode() so that needs to be made safe as well

# --- myutf8

class MyUTF8(codecs.Codec):
    def encode(self, input, errors="strict"):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors="strict"):
        return codecs.charmap_decode(input, errors, decoding_table)

class StreamWriter(MyUTF8, codecs.StreamWriter):
    pass

class StreamReader(MyUTF8, codecs.StreamReader):
    pass

def search_function(string):
    if string == "myutf8":
        return getregentry()
    return None

def getregentry():
    return codecs.CodecInfo(name="myutf8", encode=MyUTF8().encode,
                            decode=MyUTF8().decode,
                            incrementalencoder=None,

