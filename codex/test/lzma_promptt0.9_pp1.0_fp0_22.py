import lzma
# Test LZMADecompressor.__init__()

def test_lzma_init():
    cd = lzma.LZMADecompressor()
    assert cd.format is None
    assert cd.check is None
    assert cd.filters is None
    assert cd.memlimit is None
    assert cd.memlimit_hard is None
    assert cd.memlimit_soft is None
    assert cd.allocator is None
    assert cd.buffersize is None
    assert cd.eof is False
    assert cd.unused_data is None
    assert cd.unconsumed_tail is None

    # These assignments might raise AttributeError or ValueError.
    # With current implementation, they'll raise ValueError.
    try:
        cd.format = "blah"
        cd.check = "blah"
        cd.filters = "blah"
        cd.memlimit = 2**32 + 1
        cd.allocator = "blah"
    except (AttributeError, ValueError):
        pass
