import bz2
# Test BZ2Decompressor

# bz2.BZ2Decompressor
#
# class bz2.BZ2Decompressor
#
#     This class implements a decompressor object for decompressing data incrementally.
#
#     decompress(data)
#         Decompress data, returning uncompressed data as bytes.
#
#         If you use an empty bytes object as the input, the output will also be empty,
#         but if you use no input at all (or any other object not supporting the buffer
#         protocol), a ValueError will be raised.
#
#         If the input is not a multiple of 4 bytes long,
#         decompress() will raise a ValueError.
#         This is a limitation of the compression format.
#
#         After calling this function, some of the input data may still be stored in internal buffers
#         for later processing.
#         Call the flush() method to clear these buffers.
#
#     flush()
#         Flush the decompressor object.
#
#         The decompressor object can be used to decompress data incrementally.
#         After each call to the decompress
