import lzma
# Test LZMADecompressor() instances functionality.
decomp = lzma.LZMADecompressor()
b = memoryview(bytearray(1))
decomp.decompress(b, 0)

# Test LZMACompressor() instances functionality.
comp = lzma.LZMACompressor()
comp.compress(b)
comp.flush()
# Run the test suite.
import test.test_lzma
from test import support
support.run_unittest(test.test_lzma.LzmaTestCase)

# Verify reference counting.
import sys
from test.support import gc_collect
def test_refcount():
    # BytesIO.write() doesn't call tp_finalize.
    if sys.version_info[:3] == (3, 2, 4):
        return

    gc_collect()  # Clean out the garbage collector.
    import weakref
    wr = weakref.ref(memoryview(bytearray(1)).tobytes())
    assert wr() is not None

    gc_collect()  #
