from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# same as
LZMADecompressor().decompress(lzma_data[:])

# same as
LZMADecompressor().decompress(b''.join(lzma_data))

# same as
decomp = LZMADecompressor()
decomp.decompress(lzma_data[0], max_length=len(lzma_data[0]))
decomp.decompress(lzma_data[1], max_length=len(lzma_data[1]))
# etc.
</code>

