import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename, mode='rt')

import lzma
lzma.open(filename)

# 如果你想控制压缩文件的格式和压缩级别，可以直接使用模块级别的 open() 函数，
# 并传入 compresslevel 参数。比如：
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

# 如果你想操作压缩文件的元数据，比如文件名，可以使用 ZipFile 或 TarFile 来代替。
# 
