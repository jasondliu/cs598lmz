import lzma
# Test LZMADecompressor.used_data
# Test on a file with an EOF marker.
# The EOF marker is not used by the decompressor, but should be counted as used.
# The decompressor should return the correct decompressed data, and the correct
# amount of used input data.

