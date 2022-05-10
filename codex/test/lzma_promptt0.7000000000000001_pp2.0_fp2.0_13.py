import lzma
# Test LZMADecompressor's the states of stream
# state = 0: not started reading
# state = 1: reading
# state = 2: finished reading
# state = -1: error

# Decompress a file with all 0s
data = bytearray(b'\0' * 10)
