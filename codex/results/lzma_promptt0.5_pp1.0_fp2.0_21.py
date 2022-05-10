import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    for i in range(1, 9):
        for j in range(1, 40):
            for k in range(0, 8):
                for l in range(0, 4):
                    for m in range(0, 4):
                        yield check_lzma_decompressor, i, j, k, l, m

def check_lzma_decompressor(preset, length, nice_len, dict_size, lc, lp):
    # create some data to compress
    data = b'z' * length
    # compress it
    compressor = lzma.LZMACompressor(preset=preset, lc=lc, lp=lp, dict_size=dict_size, nice_len=nice_len)
    compressed = compressor.compress(data) + compressor.flush()
    # decompress it
    decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
    assert decompressor.decompress(compressed) ==
