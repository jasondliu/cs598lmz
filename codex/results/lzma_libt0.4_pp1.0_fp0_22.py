import lzma
lzma.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 进行压缩
import lzma
lzma.compress(b'hello world')

# 进行压缩
import lzma
lzma.compress(b'hello world', format=lzma.FORMAT_ALONE)

# 进行压缩
import lzma
lzma.compress(b'hello world', format=lzma.FORMAT_XZ)

# 进行压缩
import lzma
lzma.compress(b'hello world', format=lzma.FORMAT_RAW)

# 进行压缩
import lzma
lzma.compress(b
