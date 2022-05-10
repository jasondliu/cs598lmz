import lzma
lzma.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 压缩
import lzma
lzma.compress(b'hello world')

# 压缩文件
import lzma
lzma.compress(b'hello world', preset=9)

# 解压缩文件
import lzma
lzma.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 压缩
import lzma
lzma.compress(b'hello world')

# 压缩
