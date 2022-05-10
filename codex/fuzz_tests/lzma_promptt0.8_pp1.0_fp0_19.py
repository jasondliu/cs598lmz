import lzma
# Test LZMADecompressor
# decomp = lzma.LZMADecompressor()
#
# with open('bz2_file.zip', 'rb') as f_in:
#     with open('bz2_file_decompressed_no_format.txt', 'wb') as f_out:
#         for chunk in iter(lambda: f_in.read(4 * 1024**2), b''):
#             f_out.write(decomp.decompress(chunk))
#             print(decomp.eof)
#             print(decomp.unconsumed_tail)
# print(decomp.eof)
# print(decomp.unconsumed_tail)
#
# decomp.flush()
#
# with open('bz2_file_decompressed_no_format.txt', 'ab') as f_out:
#     f_out.write(decomp.unconsumed_tail)
#
#
# decomp = lzma.LZMADecompressor()
# with open('bz2_file.zip', 'rb') as f
