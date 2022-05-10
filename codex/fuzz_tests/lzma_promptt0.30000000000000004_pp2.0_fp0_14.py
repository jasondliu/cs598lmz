import lzma
# Test LZMADecompressor.decompress()

# Test decompression of a small file
with lzma.open("testdata/test1.xz", "rt") as f:
    data = f.read()
    assert data == "test 1\n"

# Test decompression of a file with multiple concatenated streams
with lzma.open("testdata/test2.xz", "rt") as f:
    data = f.read()
    assert data == "test 1\ntest 2\n"

# Test decompression of a file with multiple concatenated streams
with lzma.open("testdata/test3.xz", "rt") as f:
    data = f.read()
    assert data == "test 1\ntest 2\ntest 3\n"

# Test decompression of a file with a corrupt index
with lzma.open("testdata/test4.xz", "rt") as f:
    data = f.read()
    assert data == "test 1\ntest 2\ntest 3\n"

# Test decompression of a file with
