import bz2
bz2.BZ2File("file.bz2").read()

import gzip
gzip.open("file.gz").read()

import lzma
lzma.LZMAFile("file.xz").read()

import zipfile
z = zipfile.ZipFile("file.zip")
z.open("file.txt").read()

# ------------------------------------------------
# 二进制数据的编码和解码

s = b'Hello World'
# 解码为字符串
s.decode('ascii')

# 编码为字节
'Hello World'.encode('utf-8')

# ------------------------------------------------
# 字符串的编码和解码

# 字符串解码为字节
u = 'Hello World'
u.encode('utf-8')

