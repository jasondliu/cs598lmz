import lzma
# Test LZMADecompressor objects with various data

def check_LZMA_file(file, size, blocksize = None, check = True):
    with open(file, 'rb') as f:
        if blocksize is None:
            blocksize = size
        lz = lzma.LZMADecompressor()
        result = b''
        data = f.read(blocksize)
        while data:
            result += lz.decompress(data)
            data = f.read(blocksize)
        result += lz.flush()
        assert len(result) == size
        if check:
            data = f.read()
            assert lz.unused_data == data
            # lzma.error: Input format not specified
            # assert lz.eof == (not data)
        else:
            assert not lz.unused_data
            # lzma.error: Input format not specified
            # assert lz.eof
        # try to reuse
        result = lz.decompress(data)
        result += lz.flush()
