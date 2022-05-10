from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# The LZMADecompressor class also supports the context management protocol, 
# so you can use it in a with statement:
with LZMADecompressor() as decompressor:
    decompressor.decompress(lzma_data)

# You can also create a decompressor object and feed data to it in chunks, 
# making it useful for processing files or data streams with lzma compression:
decompressor = LZMADecompressor()
decompressor.decompress(chunk1)
decompressor.decompress(chunk2)
decompressor.decompress(chunk3)

# This class supports the buffer interface, meaning that you can read from 
# the decompressor directly into a mutable buffer (such as bytearray) with no intermediate copying:
buf = bytearray(1024)
dst = decompressor.decompress(lzma_data, buf)

# The return value is the number of bytes written to the buffer. 
# If the buffer is too small
