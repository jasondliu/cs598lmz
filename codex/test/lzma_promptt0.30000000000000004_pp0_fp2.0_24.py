import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with open('lzma_test.xz', 'rb') as f:
        d = lzma.LZMADecompressor()
        data = f.read()
        decompressed = d.decompress(data)
        assert decompressed == b'1234567890' * 1000

# Test LZMACompressor

def test_lzma_compressor():
    with open('lzma_test.xz', 'rb') as f:
        c = lzma.LZMACompressor()
        data = f.read()
        compressed = c.compress(data)
        assert compressed == data

# Test LZMADecompressor.decompress

def test_lzma_decompressor_decompress():
    with open('lzma_test.xz', 'rb') as f:
        d = lzma.LZMADecompressor()
        data = f.read()
        decompressed = d.decompress(data)
       
