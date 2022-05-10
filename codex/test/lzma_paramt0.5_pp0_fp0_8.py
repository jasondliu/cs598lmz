from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 创建一个压缩文件，写入压缩数据
import lzma
with lzma.open('file.xz', 'wt') as f:
    f.write('写入压缩的内容')

# 创建一个解压缩文件，读取压缩数据
import lzma
with lzma.open('file.xz') as f:
    file_content = f.read()
