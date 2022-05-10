import bz2
# Test BZ2Decompressor.decompress()

# Test decompressing a file

def test_decompress(filename):
    print("Decompressing {}".format(filename))
    with bz2.BZ2File(filename, "r") as f:
        data = f.read()
    with bz2.BZ2File(filename, "r") as f:
        data_bs = f.read(100)
        data_bs += f.read(100)
        data_bs += f.read()
    assert len(data) == len(data_bs)
    assert data == data_bs
    compressor = bz2.BZ2Decompressor()
    data_dc = compressor.decompress(data)
    assert len(data_dc) == len(data_bs)
    assert data_dc == data_bs
    assert compressor.unused_data == b''
    with bz2.BZ2File(filename, "r") as f:
        data_bs = f.read(1)
        data_bs += f.read(1)
        data_
