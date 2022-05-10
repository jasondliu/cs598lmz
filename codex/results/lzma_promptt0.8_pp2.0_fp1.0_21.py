import lzma
# Test LZMADecompressor
# 测试LZMADecompressor
data = lzma.open('zlib.log.xz', 'rb').read()
d = lzma.LZMADecompressor()
output = d.decompress(data)
output = d.decompress(data)
print(output)

# Test LZMAFile
# 测试LZMAFile
with lzma.open('zlib.log.xz', 'rb') as f1:
    with open('zlib.log', 'wb') as f2:
        f2.write(f1.read())

# Test compress
# 测试压缩
data = b'The quick brown fox jumps over the lazy dog.' * 10
compressed = lzma.compress(data, preset=9 | lzma.PRESET_EXTREME)
decompressed = lzma.decompress(compressed)
print(decompressed == data)

# Test compressfile
# 测试压缩文
