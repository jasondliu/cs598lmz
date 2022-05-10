import lzma
lzma.compress(b"hello world!")

"""
Compress the bytes object b and return a bytes object containing compressed data for at least size bytes.
If size is negative or omitted, return a bytes object containing compressed data with no size limit.
"""

lzma.decompress(b"x\x9c+\xcf\xcfH\xcd\xc9\xc9\x07\x00\x06,V\x02\x00 \x08\x85\x10\x05\x00\x00\x00")

"""
Decompress the data previously compressed by compress() or an incompatible data format.
The resulting data will be returned as a bytes object.
"""

lzma.LZMADecompressor()

"""
Return a decompressor object to be used for decompressing data incrementally.
"""

lzma.LZMACompressor()

"""
Return an compressor object to be used to compress data incrementally.
"""

lzma.LZMAFile(fileobj=None, mode=None)

"""
Return
