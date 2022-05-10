import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with open('../test/data/lzma/lzma_alone_decompress.bin', 'rb') as f:
        data = f.read()
    decompressor = lzma.LZMADecompressor()
    assert decompressor.decompress(data) == b'hello world!hello world!hello world!hello world!'

def test_lzma_decompressor_unused_data():
    with open('../test/data/lzma/lzma_alone_decompress.bin', 'rb') as f:
        data = f.read()
    decompressor = lzma.LZMADecompressor()
    assert decompressor.decompress(data, max_length=20) == b'hello world!hello world!'
    assert decompressor.unused_data == data[20:]

