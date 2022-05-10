import lzma
# Test LZMADecompressor to ensure we can decompress the chunk
# NOTES:
#  * The output is a generic stream of bytes, not a string.
#
#  * If the source is a file object, the current position
#    in the file will be used as input data. When the end
#    of the compressed data is reached, the position will
#    be reset back to the original position.
#
#  * If you want to decompress data sequentially, decompressor.decompress()
#    must always be called with zero length, and decompressor.eof must be
#    checked between calls.
#
#  * If you want to decompress data in one call, use decompressor.decompress(data),
#    where data is a bytes object with the whole compressed data stream.
#    In this case the decompressor’s eof property should not be checked.
#    Note that the decompress() method may not return the entire
#    decompressed data stream. Call it repeatedly until it returns an empty bytes object.
#
#  * The decompressor.flush() method can be used to get any remaining data
#
