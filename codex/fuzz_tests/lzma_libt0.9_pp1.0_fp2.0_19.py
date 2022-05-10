import lzma
lzma.block_buffer_limit(1 << 30)
from nose.tools import assert_raises_regexp

from lzma import LZMADecompressor as _LZMADecompressor
import lzma
lzma.block_buffer_limit(1 << 30)
from nose.tools import assert_raises_regexp
MAX_SIZE = 1048576
COMPRESSED_SIZE = 81920
COPY_LENGTH = 1000
TEST_DATA = b"1234567890" * COPY_LENGTH


def test_accesses_through_contextmanager():
    c = lzma.LZMACompressor(check=-1, preset=6)

    with c as compressor:
        compressed = compressor.compress(TEST_DATA)
        compressed += compressor.flush()

    with lzma.LZMADecompressor(check=-1) as decompressor:
        assert_raises_regexp(
            IOError,
            "Can't use .* after context closed",
            decompressor.__setattr__,
           
