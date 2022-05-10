import lzma
lzma.compress(b"hello world!")

"""
Compress the bytes object b and return a bytes object containing compressed data for at least size bytes.
If size is negative or omitted, return a bytes object containing compressed data with no size limit.
"""

