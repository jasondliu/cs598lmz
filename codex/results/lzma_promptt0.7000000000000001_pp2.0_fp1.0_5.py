import lzma
# Test LZMADecompressor
def test_lzma_decompressor():
    # Test normal
    with lzma.LZMADecompressor() as decomp:
        compressed_data = b'x\x9c\x0b\x90\xabj\x04\x00\x01J\x04'
        expected_data = b'This is the original data.'
        assert decomp.decompress(compressed_data) == expected_data

    # Test streaming decompression
    with lzma.LZMADecompressor() as decomp:
        compressed_data = b'x\x9c\x0b\x90\xabj\x04\x00\x01J\x04'
        expected_data = b'This is the original data.'
        assert decomp.unconsumed_tail == b''
        assert decomp.decompress(compressed_data[:5], max_length=5) == b''
        assert decomp.unconsumed_tail == compressed_data[:5]
        assert decomp.decompress(compressed_data[5:])
