import lzma
# Test LZMADecompressor with a known test file

test_file = "lzma_test_file.lzma"

with lzma.open(test_file) as f:
    c = f.read()

d = lzma.LZMADecompressor()

with d.streamreader(c) as r:
    assert r.read() == b"Hello, world!"
 
# Test LZMADecompressor with a known test file

test_file = "lzma_test_file.lzma"

with lzma.open(test_file) as f:
    c = f.read()

d = lzma.LZMADecompressor()

with d.streamreader(c) as r:
    assert r.read() == b"Hello, world!"
 
# Test LZMADecompressor with a known test file

test_file = "lzma_test_file.lzma"

with lzma.open(test_file) as f:
    c = f.read()


