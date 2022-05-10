import lzma
lzma.LZMAError

import pytest

from . import util

def test_lzma_compression():
    data = b'\x00' * 100

    compressed = lzma.compress(data)
    assert len(compressed) < len(data)

    decompressed = lzma.decompress(compressed)
    assert decompressed == data

def test_lzma_compression_level():
    data = b'\x00' * 100

    for level in range(10):
        compressed = lzma.compress(data, preset=level)
        decompressed = lzma.decompress(compressed)
        assert decompressed == data

def test_lzma_compression_filters():
    data = b'\x00' * 100

    for filters in [
        {'id': lzma.FILTER_LZMA1, 'dict_size': 2 ** 16},
        {'id': lzma.FILTER_LZMA2, 'dict_size': 2 ** 16},
        {
