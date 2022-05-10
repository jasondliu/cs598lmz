import lzma
# Test LZMADecompressor with a small, known-good file.

with open('test/testdata/test1.xz', 'rb') as f:
    with lzma.open(f, format=lzma.FORMAT_ALONE) as xf:
        data = xf.read()
        assert data == b'1234567890' * 1000
# Test LZMADecompressor with a large, known-good file.

with open('test/testdata/test2.xz', 'rb') as f:
    with lzma.open(f, format=lzma.FORMAT_ALONE) as xf:
        data = xf.read()
        assert len(data) == 100000000
        assert data[:4] == b'\x00\x00\x00\x00'
        assert data[-4:] == b'\xff\xff\xff\xff'
# Test LZMADecompressor with a file that has a corrupted index.

with open('test/testdata/test3.xz', 'rb') as f:
    with
