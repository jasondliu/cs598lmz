import codecs
codecs.register_error('strict', codecs.ignore_errors)


class JSONIStream(object):
    r"""
    持续无缓冲(!)的JSON数据解析，分行模式
    Iterative JSON Stream Decoder
    """

    @classmethod
    def split(cls):
        return '\r\n'

    @classmethod
    def ignored_chars(cls):
        return tuple(map(chr, range(0, 256)))

    @classmethod
    def join(cls):
        return cls.split()

    @classmethod
    def encoder(cls):
        return 'unicode-escape'

    @classmethod
    def decoder(cls):
        return 'strict'

    __slots__ = ()

    def __init__(self, fileobj, splitter=split(), encoder=encoder(), decoder=decoder()):
        self.fileobj = fileobj
        self.splitter = splitter.encode(enc
