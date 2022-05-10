from lzma import LZMADecompressor
LZMADecompressor.decompress(compressed).decode()

# note that the input must be bytes, not a string, so we need to use the .encode() method
compressed = b'\xfdSM\x00\x00\x04\xe6\xd6+HIT\x01\x00!\x9ch\x1c\xc9\xc8,\x04\x00\x00\x00\n'
LZMADecompressor().decompress(compressed)

# you can also use the LZMADecompressor.decompress() method to decompress multiple chunks
decompressor = LZMADecompressor()
chunk1 = b'\x00\x00\x00\x07\x00\x00\x00\x00'
chunk2 = b'\xff\xff\xff\xff\xff\xff\xff\xff'
decompressor.decompress(chunk1)
decompressor.decompress(chunk2)

# when the decompressor reaches the end of the stream, it raises an
