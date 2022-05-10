import lzma
lzma.decompress(open('xz/data.xz', 'rb').read())

# xz方式解压
import lzma
with open('xz/data.xz', 'rb') as f:
    file_content = lzma.decompress(f.read())

# 解压后的数据量
len(file_content)

# 使用更宽松的模式进行解压
import lzma
with open('xz/data.xz', 'rb') as f:
    file_content = lzma.decompress(f.read(), format=lzma.FORMAT_RAW, memlimit=2 ** 30)

# 打包成tar.xz
import lzma
import tarfile
with tarfile.open('xz/test.xz', 'w:xz') as tr:
    tr.add('xz/data.xz')

# 解
