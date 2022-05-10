import lzma
lzma.open("archive.lzma")

#zlib
import zlib
zlib.decompress("archive.zlib")

#bzip2
import bz2
bz2.open("archive.bz2")

#lz4
import lz4
lz4.decompress("archive.lz4")

#snappy
import snappy
snappy.uncompress("archive.sz")

#brotli
import brotli
brotli.decompress("archive.br")

import py_compile
py_compile.compile("archive.pyc")

#java
import java.util.zip.GZIPInputStream
import java.io.FileInputStream
import java.io.FileOutputStream
import java.io.BufferedOutputStream

fis = FileInputStream("archive.gz")
gzip = GZIPInputStream(fis)
bos = BufferedOutputStream(FileOutputStream("archive.tar"))
b = [0] * 1024
while True:
    n = gzip.
