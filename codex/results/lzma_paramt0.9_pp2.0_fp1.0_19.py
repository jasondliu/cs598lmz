from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\3+\0\0\0\2\0\0\0\4\4\4')

class LZMADecompressor(DecompressWrap):
    eof = False

    def __init__(self, *args, **kwargs):
        self.obj = LZMACompressor(*args, **kwargs)

    def decompress(self, data=None, max_length=None):
        if self.eof:
            raise EOFError('End of stream already reached')
        super().decompress(data, max_length)

    def flush(self, max_length=None):
        return b''

    def __getstate__(self):
        state = super().__getstate__()
        del state['obj'].check
        return state

class LZMADecompressor(LZMACompressor):

    def __init__(self, format=FORMAT_AUTO, check=-1, dict_size=None,
                 filters=None):
        super().__init__(format, check, dict
