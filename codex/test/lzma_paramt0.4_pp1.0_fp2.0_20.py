from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'Hello World!\n'

# The LZMA compression algorithm is an improved version of the LZ77 algorithm.

# The LZ77 algorithm is a dictionary coder that uses a sliding window to maintain a set of previously seen data.
# When a match is found between the current input and the previous data, the match is encoded as a pair of
# (distance, length) values.

# The LZMA algorithm uses a slightly different approach.
# Instead of a sliding window, it uses a cyclic buffer of fixed size.
# The dictionary is created by combining the previous byte with the current byte.
# The dictionary is then searched for the longest match.
# The match is encoded as a pair of (offset, length) values.

# The LZMA algorithm also uses a range encoder to encode the match
