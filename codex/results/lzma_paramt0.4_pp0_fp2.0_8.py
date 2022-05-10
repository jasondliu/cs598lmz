from lzma import LZMADecompressor
LZMADecompressor.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# 压缩数据
comp = LZMACompressor()
comp.compress(b'123')
comp.compress(b'456')
comp.flush()

# 解压缩数据
decomp = LZMADecompressor()
decomp.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
