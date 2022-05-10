import codecs
# Test codecs.register_error()

class bogus_re(object):

    def __init__(self, encoding):
        self.encoding = encoding

    def getregentry(self):
        return codecs.CodecInfo(
            name = self.encoding,
            encode = self.encode,
            decode = self.decode,
            )

    def decode(self, str):
        return ('', 2)

    def encode(self, str):
        return ('', 2)

class bogus_re_return_str(object):

    def __init__(self, encoding):
        self.encoding = encoding

    def getregentry(self):
        return codecs.CodecInfo(
            name = self.encoding,
            encode = self.encode,
            decode = self.decode,
            )

    def decode(self, str):
        return ('yowza', 3)

    def encode(self, str):
        return ('yowza' * 5, 4)


c1 = bogus_re('bogus_re')
c2 = bogus_re_
