import lzma
# Test LZMADecompressor
#
# The LZMADecompressor class reads LZMA compressed data from a stream
# and returns uncompressed data as bytes objects.
#
# Example:
#
#     with open("compressed.lzma", "rb") as input:
#         decompressor = LZMADecompressor()
#         while True:
#             chunk = input.read(64 * 1024)
#             if len(chunk) == 0:
#                 break
#             output = decompressor.decompress(chunk)
#             if output:
#                 process_uncompressed_data(output)
#         remaining = decompressor.flush()
#         if remaining:
#             process_uncompressed_data(remaining)
#
# This example could be reimplemented using the decompress() function.
#
# The LZMADecompressor class has the following public methods:
#
# decompress(data)
#     Reads LZMA compressed data from the bytes object *data*, returns
#     a bytes object containing the uncompressed data, or an empty
#     bytes
