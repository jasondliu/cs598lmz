import lzma
# Test LZMADecompressor obj

@stream_capture(capture_stdout=True, capture_stderr=True)
def test_LZMADecompressor_object():
    with lzma.LZMADecompressor() as compressor:
        compressor.decompress(COMPRESSED_TEXT)
        compressor.flush()


@stream_capture(capture_stdout=True, capture_stderr=True)
def test_LZMADecompressor_object_use_after_close():
    with lzma.LZMADecompressor() as compressor:
        pass
    try:
        compressor.decompress(COMPRESSED_TEXT)
        assert 0, "should not get here"
    except ValueError as e:
        assert "closed" in str(e)


@stream_capture(capture_stdout=True, capture_stderr=True)
def test_LZMADecompressor_object_context_manager():
    with lzma.LZMADecompressor() as compressor:
        decompressed = compressor
