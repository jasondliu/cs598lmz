import bz2
bz2.BZ2File(path, 'r')

import gzip
gzip.GzipFile(path, 'r')

with open(path, 'rb') as f:
    f.read()

# 如果是一个压缩的文件，但是不知道是用哪种压缩方式压缩的，可以使用以下方法来检测
import bz2, gzip, lzma, zipfile

extension_map = {
    '.bz2': bz2.BZ2File,
    '.gz': gzip.GzipFile,
    '.xz': lzma.LZMAFile,
    '.zip': zipfile.ZipFile
}

for ext, opener in extension_map.items():
    try:
        filename = path + ext
        f = opener(filename, 'rb')
    except (IOError, zipfile.BadZip
