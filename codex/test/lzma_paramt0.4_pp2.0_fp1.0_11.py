from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# lzma.LZMADecompressor.decompress(data, max_length=-1)
#
# Decompress *data*, returning uncompressed data as bytes.
#
# If *max_length* is nonnegative, returns at most *max_length* bytes of
# decompressed data. If this limit is reached and further output can be
# produced, *self.needs_input* will be set to ``False``. In this case, the next
# call to *decompress()* may provide *data* as b'' to obtain more of the output.
#
# If all of the input data was decompressed and returned (either because this
# was less than *max_length* bytes, or because *max_length* was negative),
# *self.needs_input* will be set to
