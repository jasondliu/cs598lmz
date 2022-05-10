import lzma
# Test LZMADecompressor

def roundtrip_decompressor(decompressor, data, max_length=None):
    # make sure that the roundtrip data is equal to the original data
    decompressed = decompressor.decompress(data, max_length)
    rest = decompressor.unused_data
    decompressor.reset()
    if rest:
        # decompressor.unused_data should be empty if the whole data was decompressed
        decompressed2 = decompressor.decompress(rest)
        assert decompressed == decompressed2

    # check .flush() with empty data
    flushed = decompressor.flush()
    assert flushed == b""
    rest = decompressor.unused_data
    decompressor.reset()
    if rest:
        # decompressor.unused_data should be empty if the whole data was decompressed
        flushed2 = decompressor.flush()
        assert flushed == flushed2

    # check .flush() with some data
    decompressed = decompressor.decompress(data, max_length)
    flushed = decompressor.flush()
    decompressor.reset()
