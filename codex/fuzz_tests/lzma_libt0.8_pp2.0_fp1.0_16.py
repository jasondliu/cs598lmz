import lzma
lzma_compressor = lzma.LZMACompressor()
# Append bytes to the compressor object
lzma_compressor.compress(b"foo")
# Returns the compressed data so far, as a bytes object.
lzma_compressor.flush()
# Returns the bytes left after decompressing
lzma_compressor.unused_data
# When the compressor object was created with `format=lzma.FORMAT_RAW`,
# the method returns a bytes object with the stream header.
# Otherwise, it returns the empty bytes object.
lzma_compressor.stream_header

lzma_decompressor = lzma.LZMADecompressor()
lzma_decompressor.decompress(bytes_data)
lzma_decompressor.unused_data
# When the decompressor object was created with `format=lzma.FORMAT_RAW`,
# the method returns a bytes object with the stream header.
# Otherwise, it returns the empty bytes object.
lzma_decompressor.stream_header


# Pickling
