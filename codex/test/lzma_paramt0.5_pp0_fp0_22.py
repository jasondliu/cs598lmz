from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 对于比较大的数据，使用一个压缩文件可能更有用，可以使用lzma模块的open()函数打开一个压缩文件，
# 就像是使用open()函数打开一个普通文件一样。
import lzma
with lzma.open('lzma_compressed.xz', 'rt') as f:
    text = f.read()

# 你可以指定一个
