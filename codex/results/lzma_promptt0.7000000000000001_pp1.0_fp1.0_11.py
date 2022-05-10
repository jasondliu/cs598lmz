import lzma
# Test LZMADecompressor
with open('../tests/testdata/lzma_alone_compressed', 'rb') as f:
    header_size = lzma.LZMADecompressor().get_header_size(f.read(lzma.HEADER_SIZE))
    with open('../tests/testdata/lzma_alone_compressed', 'rb') as g:
        with lzma.LZMADecompressor() as decomp:
            decomp.decompress(g.read(header_size))
            # get_header_size() seems to be broken with the lzma module.
            # It never returns the actual header size, so we have to
            # check it manually.
            if header_size != lzma.HEADER_SIZE and header_size != lzma.HEADER_SIZE + 1:
                raise RuntimeError("header_size is %d" % header_size)

# Test LZMACompressor
with open('../tests/testdata/lzma_alone_compressed', 'rb') as f:
    with lzma.LZ
