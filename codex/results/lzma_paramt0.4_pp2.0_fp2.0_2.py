from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 压缩数据
data = b'Lots of data here'
with lzma.open('compress.xz', 'w') as f:
    f.write(data)

# 压缩数据
with lzma.open('compress.xz', 'w', preset=9) as f:
    f.write(data)

# 压缩数据
with lzma.open('compress.xz', 'w', preset=9 | lzma.PRESET_EXTREME) as f:
    f.write(data)

# 压缩数据
with lzma.open('compress.xz', 'w', preset=0, filters=[
    {"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME}
]) as f:
    f.write(data)

# 读取数据

