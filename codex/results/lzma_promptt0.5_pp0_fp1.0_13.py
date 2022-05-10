import lzma
# Test LZMADecompressor
# x = lzma.LZMADecompressor()
# print(x.decompress(lzma_data))

# Test LZMAFile
# with lzma.open('/tmp/test.lzma', 'rb') as f:
#     file_content = f.read()
# print(file_content)

# Test LZMAFile for writing
# with lzma.open('/tmp/test.lzma', 'wb') as f:
#     f.write(b'hello world\n')

# Test LZMAFile for writing with preset
# with lzma.open('/tmp/test.lzma', 'wb', preset=9 | lzma.PRESET_EXTREME) as f:
#     f.write(b'hello world\n')

# Test LZMAFile for writing with filters
# with lzma.open('/tmp/test.lzma', 'wb', preset=9 | lzma.PRESET_EXTREME, filters={'id': lzma.FILTER_
