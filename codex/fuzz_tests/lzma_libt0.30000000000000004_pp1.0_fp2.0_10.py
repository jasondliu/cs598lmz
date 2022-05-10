import lzma
lzma.LZMAError

import pytest

from . import util


def test_compress_decompress():
    # Compress and decompress some data.
    data = b"Hello world!"
    compressed = lzma.compress(data)
    assert compressed != data
    assert lzma.decompress(compressed) == data

    # Compress and decompress some more data.
    data = b"Hello world! " * 100
    compressed = lzma.compress(data)
    assert compressed != data
    assert lzma.decompress(compressed) == data


def test_compress_decompress_with_filters():
    # Compress and decompress some data with a filter chain.
    data = b"Hello world!"
    compressed = lzma.compress(data, format=lzma.FORMAT_RAW,
                               filters=[{"id": lzma.FILTER_LZMA2,
                                         "preset": 9 | lzma.PRESET_EXTREME}])
    assert compressed != data
