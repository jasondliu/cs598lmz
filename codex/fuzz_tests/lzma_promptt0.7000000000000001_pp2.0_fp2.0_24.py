import lzma
# Test LZMADecompressor with no start_of_stream=True,
# to see the error raised by the C layer
import pytest

from test import support
from test.support import bigmemtest


def test_read_consumes_input():
    in_data = b'foo a b c ' * 10
    compressor = lzma.LZMACompressor()
    out = compressor.compress(in_data)
    out += compressor.flush()
    del compressor
    decompressor = lzma.LZMADecompressor()
    buf = io.BytesIO(out)
    f = lzma.LZMAFile(buf)
    assert f.read() == in_data
    f.close()
    assert buf.tell() == len(out)


def test_readline():
    in_data = b'foo\na bar\nbaz\n'
    compressor = lzma.LZMACompressor()
    out = compressor.compress(in_data)
    out += compressor.flush()
    del compressor
    buf = io.BytesIO(out)
   
