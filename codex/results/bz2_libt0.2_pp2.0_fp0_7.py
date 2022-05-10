import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename, mode='rt')

import lzma
lzma.open(filename)

# 如果你想控制压缩格式和压缩级别，可以使用 zipfile 模块来代替
import zipfile
zf = zipfile.ZipFile(filename)
zf.extractall(path='/some/directory')
zf.close()

# 如果你想创建一个 ZIP 文件，可以这样做
import zipfile
zf = zipfile.ZipFile(filename, mode='w')
zf.write(filename)
zf.close()

# 如果你想控制 ZIP 压缩级别，可以这
