import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with open('lzma_data', 'rb') as f:
        data = f.read()
    with lzma.LZMADecompressor() as decompressor:
        result = decompressor.decompress(data)
    assert result == b'Hello World!\n'

def test_lzma_decompressor_with_eos():
    with open('lzma_data', 'rb') as f:
        data = f.read()
    with lzma.LZMADecompressor() as decompressor:
        result = decompressor.decompress(data, max_length=12)
    assert result == b'Hello World!\n'

def test_lzma_decompressor_with_eos_and_unused_data():
    with open('lzma_data', 'rb') as f:
        data = f.read()
    with lzma.LZMADecompressor() as decompressor:
        result = decompressor.decompress
