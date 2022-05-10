from lzma import LZMADecompressor
LZMADecompressor()

# 用于解压 gzip 文件的类
from gzip import GzipFile
GzipFile(filename=None, mode=None, compresslevel=None)

# 用于解压 bz2 文件的类
from bz2 import BZ2Decompressor
BZ2Decompressor()

# 用于解压 tar 归档文件的类
from tarfile import TarFile
TarFile(name=None, mode=None, fileobj=None, format=None, tarinfo=None, dereference=False, ignore_zeros=True, encoding=None, errors=None, pax_headers=None, debug=0, errorlevel=0, strict_gnu=False, **kwargs)
 
# 用于解压 zip 文件的类
from zipfile import ZipFile
ZipFile(file, mode='r', compression=None, allowZip64=True)
