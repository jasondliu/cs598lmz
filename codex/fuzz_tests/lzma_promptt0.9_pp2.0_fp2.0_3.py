import lzma
# Test LZMADecompressor

# decompressor = lzma.LZMADecompressor()
# for chunk in chunks:
#     out += decompressor.decompress(chunk)
# print('final footprint of uncompressed data:', len(out))
# assert out == (original * 5)
# assert decompressor.unused_data == b''

# Alternatively, can supply multiple data chunks to decompress() method:
# out = b''
# decompressor = lzma.LZMADecompressor()
# out = decompressor.decompress(b''.join(chunks))
# assert out == (original * 5)
# assert decompressor.unused_data == b''

# Alternatively, use decode() method to output as a Unicode str:
# decompressor = lzma.LZMADecompressor()
# output = b''.join(chunks)
# out = decompressor.decode(output, 'utf-8', errors='replace')
# assert out == original * 5
# assert decompressor.unused_data == b''

# Test LZMAFileType
#
