import bz2
# Test BZ2Decompressor
# decompressor = bz2.BZ2Decompressor()
# with open('data/compressed.bz2', 'rb') as input:
#     with open('data/uncompressed.txt', 'wb') as output:
#         for block in iter(lambda: input.read(100 * 1024), b''):
#             output.write(decompressor.decompress(block))
#             if not decompressor.eof:
#                 raise EOFError('Compressed file ended before the '
#                                'end-of-stream marker was reached.')

# Test BZ2Compressor
