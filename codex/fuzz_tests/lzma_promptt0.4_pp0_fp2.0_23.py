import lzma
# Test LZMADecompressor

with lzma.open('../../lzma_test_files/test.xz', 'rb') as infile:
    with lzma.open('../../lzma_test_files/test_decomp_lzma.txt', 'wb') as outfile:
        decomp = lzma.LZMADecompressor()
        while True:
            chunk = infile.read(1024)
            if not chunk:
                break
            outfile.write(decomp.decompress(chunk))
        outfile.write(decomp.flush())
# Test LZMADecompressor with multiple filters

with lzma.open('../../lzma_test_files/test_filters.xz', 'rb') as infile:
    with lzma.open('../../lzma_test_files/test_decomp_lzma_filters.txt', 'wb') as outfile:
        decomp = lzma.LZMADecompressor()
        while True:
            chunk = infile.read(1024
