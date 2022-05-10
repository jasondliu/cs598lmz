from lzma import LZMADecompressor
LZMADecompressor().decompress(
    b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00")

# decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)
#     data: bytes-like object

#     format:
#         FORMAT_XZ (default): Data is an XZ stream.
#         FORMAT_ALONE: Data is a single compressed .xz file.
#         FORMAT_RAW: Data is in the raw compressed format.

#     memlimit:
#         Maximum amount of memory (in kibibytes) that the decompressor
#         can use at a time.
#         The default is the uncompressed size of the input data,
#         which means that no memory is allocated outside the internal
#         buffers
