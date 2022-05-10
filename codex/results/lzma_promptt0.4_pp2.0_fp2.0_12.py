import lzma
# Test LZMADecompressor

# The first three bytes of the stream are the header
# (three bytes are used because some bit fields in header
# are reserved and set to zero).

# The header is decoded as follows:

# Offset   Size    Description
#   0      1       lc, lp and pb in encoded form.
#   1      1       dict_size in encoded form.
#   2      4       uncompressed size.
#   6      4       reserved, must be 0.

# The header is followed by the compressed data.

class LZMADecompressor:
    def __init__(self, data):
        self.data = data
        self.lc = 0
        self.lp = 0
        self.pb = 0
        self.dict_size = 0
        self.uncompressed_size = 0
        self.reserved = 0
        self.decode_header()

    def decode_header(self):
        self.lc = (self.data[0] & 0x1F) + 1
        self.lp = ((self.data[0] & 0
