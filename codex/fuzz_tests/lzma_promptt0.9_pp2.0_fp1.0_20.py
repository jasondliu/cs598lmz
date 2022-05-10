import lzma
# Test LZMADecompressor
C = LZMADecompressor()
stream = C.decompress(lzma_data)
print(stream == uncomp_data)

##
# Test the Compressor class
C = LZMACompressor(format=FORMAT_RAW)
stream_raw = C.compress(data)
C = LZMACompressor(format=FORMAT_XZ)
stream_xz = C.compress(data)
# The raw compressed data isn't usable on its own, but all usable lzma
# compressed data is a prefix of the raw compressed data.
print(stream_raw == stream_xz + bytes(len(stream_raw) - len(stream_xz)))
# The xz-utils format requires an integrity check, so the data is not
# usable until it is concatenated with the stream footer.
# This is not a complete implementation of the xz-utils format.
stream_xz = stream_xz + LZMAEncoder(FORMAT_XZ, check=CHECK_CRC32).end_stream()
# Test LZMADecomp
