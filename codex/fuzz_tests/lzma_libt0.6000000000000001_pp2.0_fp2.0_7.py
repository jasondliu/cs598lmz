import lzma
lzma.decompress(lzma.compress('Hello World!'))

# 文件压缩
import gzip
import shutil
with gzip.open('file.txt.gz', 'wt') as f:
    f.write('Contents of the example file go here.\n')
with gzip.open('file.txt.gz', 'rt') as f:
    text = f.read()

# 压缩文件
shutil.make_archive('archive', 'gztar', root_dir='.')

# 解压缩文件
shutil.unpack_archive('archive.tar.gz', 'final', 'gztar')

# 列出压缩文件内容
with gzip.open('file.txt.gz', 'rt') as f:
    print(f.read(10))

# 将数据写入压缩文件
with gzip.open('file.txt.
