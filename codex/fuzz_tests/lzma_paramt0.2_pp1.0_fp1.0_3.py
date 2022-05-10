from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 压缩数据
compressor = LZMACompressor()
compressor.compress(b'Some data')
compressor.flush()

# 压缩文件
with open('file.xz', 'wb') as f:
    with LZMACompressor(f) as compressor:
        compressor.write(b'Some data')

# 解压文件
with open('file.xz', 'rb') as f:
    with LZMADecompressor(f) as decompressor:
        decompressor.read()

# 压缩文件
with open('file.xz', 'wb') as f:
    with LZMACompressor(f, format=lzma.FORMAT_ALONE) as compressor:
        compressor.write(b'Some data')

# 解压文件
with open('file.xz', 'rb') as f:
    with LZMADecompressor(f, format
