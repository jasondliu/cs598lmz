from lzma import LZMADecompressor
LZMADecompressor.__module__

import sys
sys.modules['lzma'] = _lzma
import lzma

from lzmaffi import LZMADecompressor
del sys.modules['lzmaffi']

import sys
sys.modules['lzma'] = _lzma
del _lzma

import pytest

@pytest.fixture(params=[
    b'\x00',
    b'\x00' * 100,
    b'\x00' * 100 * 1024,
    b'\x00' * 100 * 1024 * 1024,
    b'\x00' * 100 * 1024 * 1024 * 1024,
])
def data(request):
    return request.param

def test_decompressor_init(data):
    d = LZMADecompressor()
    d.decompress(data)

def test_decompressor_reset(data):
    d = LZMADecompressor()
    d.decompress(data)
    d.reset()
    d.decompress
