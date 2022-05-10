import codecs
# Test codecs.register_error

def unquote(s):
    return codecs.getdecoder("quoted-printable")(s)[0]


def unhex(s):
    return codecs.getdecoder("hex-codec")(s)[0]


class MyUnquote(codecs.Codec):
    def decode(self, s, errors="strict"):
        return unquote(s), len(s)

    def encode(self, s, errors="strict"):
        return codecs.quoted_printable_encode(s), len(s)

def getregentry():
    return codecs.CodecInfo(
        name="unquote",
        encode=MyUnquote().encode,
        decode=MyUnquote().decode,
        incrementalencoder=None,
        incrementaldecoder=None,
        streamreader=None,
        streamwriter=None,
    )

codecs.register(getregentry)

def unhexlify(s):
    return codecs.getdecoder("hexlify")(s)[0]
