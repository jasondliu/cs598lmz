from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# compress()
# Returns a bytes object containing compressed data.

# flush()
# Returns a bytes object containing any remaining compressed data.

# copy()
# Returns a copy of the decompressor object. This can be used to save the state of the decompressor so that you can
#  feed new data into it.
