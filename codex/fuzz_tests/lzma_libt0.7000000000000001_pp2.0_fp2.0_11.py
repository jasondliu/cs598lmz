import lzma
lzma.open

class _LZMACompressor(io.RawIOBase):
    def __init__(self, format=FORMAT_ALONE, check=-1, preset=None, filters=None):
        self._output = io.BytesIO()
        self._compressor = lzma.LZMACompressor(format, check, preset, filters)

    def read(self, size=-1):
        return self._output.getvalue()

    def close(self):
        self._compressor.close()
        self._output.close()

    def write(self, data):
        self._output.write(self._compressor.compress(data))

class _LZMADecompressor(io.RawIOBase):
    def __init__(self, format=FORMAT_AUTO, memlimit=None, filters=None):
        self._input = io.BytesIO()
        self._decompressor = lzma.LZMADecompressor(format, memlimit, filters)

    def read(self, size=-1):
        return self._dec
