import lzma
# Test LZMADecompressor.decompress with a block size of 1

def test_decompress_block_size_1():
    data = b'\x5d\x00\x00\x80\x00\xff'
    with lzma.LZMADecompressor() as dec:
        assert dec.decompress(data) == b'\x0a' * 255
        assert dec.eof is True
        assert dec.unused_data == b''

# Test LZMADecompressor.decompress with a block size of 2

def test_decompress_block_size_2():
    data = b'\x5d\x00\x00\x80\x00\xff'
    with lzma.LZMADecompressor() as dec:
        assert dec.decompress(data[:2]) == b''
        assert dec.eof is False
        assert dec.unused_data == b''
        assert dec.decompress(data[2:], max_length=1) == b'\x0a'

