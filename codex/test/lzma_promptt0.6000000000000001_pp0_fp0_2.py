import lzma
# Test LZMADecompressor class

def test_lzma_decompressor():
    # Check that the decompressor can handle a variety of input sizes
    for size in [0, 1, 2, 3, 4, 5, 15, 16, 17, 31, 32, 33, 1023, 1024, 1025]:
        data = b' ' * size
        cdata = lzma.compress(data)
        d = lzma.LZMADecompressor()
        assert d.decompress(cdata) + d.flush() == data
        assert d.unused_data == b''

    # Check that the decompressor can handle a variety of input chunks
    def gen_chunks(n):
        for i in range(n):
            yield b' ' * i

    for n in [1, 2, 3, 4, 5, 15, 16, 17, 31, 32, 33, 1023, 1024, 1025]:
        data = b''.join(gen_chunks(n))
        cdata = lzma.compress(data)
        d = lzma.LZMAD
