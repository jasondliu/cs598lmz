from lzma import LZMADecompressor
LZMADecompressor().decompress(f.read())

# 从gzip文件读取数据
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# 创建一个带有额外选项的gzip压缩文件
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

# 在内存中压缩数据
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)

# 以块的形式对二进制数据进行压缩
import zlib
t = zlib.compress(s, 6)
zlib.decompress(t
