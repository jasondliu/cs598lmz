from lzma import LZMADecompressor
LZMADecompressor.__module__ = '_lzma'

class _LzmaDecompressor(object):
    def __init__(self, *args, **kwargs):
        self._decompressor = LZMADecompressor(*args, **kwargs)

    def decompress(self, data):
        return self._decompressor.decompress(data)


class _LzmaDecompressor_XZ(object):
    def __init__(self, *args, **kwargs):
        self._decompressor = LZMADecompressor_XZ(*args, **kwargs)

    def decompress(self, data):
        return self._decompressor.decompress(data)


class _LzmaDecompressor_MultiCall(object):
    def __init__(self, *args, **kwargs):
        self._decompressor = LZMADecompressor_MultiCall(*args, **kwargs)

    def decompress(self, data):
        return self._decompressor.decompress(data)


class _L
