from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00')

# Output: b'\xaa\xbb\xcc\xdd'


# LZMAEncoder and LZMADecoder classes
# The LZMAEncoder and LZMADecoder classes provide a streaming interface
# for compressing and decompressing data.
# The LZMAEncoder class is a context manager that can be used with the
# with statement to simplify the use of the encoder.
# The LZMADecoder class is a context manager that can be used with the
# with statement to simplify the use of the decoder.

