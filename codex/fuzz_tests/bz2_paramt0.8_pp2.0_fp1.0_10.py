from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\xc8N\x18\x00\x00\x00\x00\x00\x01\xad\xac\x8b\xea\x05l\xa6\x03\x8c4')

# The function, bz2.decompress(data), takes a single byte string as its argument and returns a single byte string as its output.
# The input argument can be any length, but the output will always be slightly larger than the input.
# In this example, we decode the text string and store the result in the variable, uncompressed_text.
# We subsequently print the first 500 characters of the decompressed output to demonstrate that it has successfully been decompressed.

# BZ2Decompressor().decompress(b'BZh91AY&SY\xc8N\x18\x00\x00\x00\x00\x00\x01\xad\xac\x8b\xea\x05l\xa6\x03\x8c4')

import bz2

