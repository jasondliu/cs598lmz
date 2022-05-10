import lzma
lzma.LZMAError

import pytest

from . import util

class TestLZMA:
    def test_compress_decompress(self):
        data = b'1234567890' * 100000
        for level in range(0, 10):
            compressed = lzma.compress(data, level)
            assert lzma.decompress(compressed) == data

    def test_compress_decompress_filter_preset(self):
        data = b'1234567890' * 100000
        for level in range(0, 10):
            compressed = lzma.compress(data, level, preset=9 | lzma.PRESET_EXTREME)
            assert lzma.decompress(compressed) == data

    def test_compress_decompress_filter_params(self):
        data = b'1234567890' * 100000
        for level in range(0, 10):
            compressed = lzma.compress(data, level,
                                       filters=[{"id": lzma.
