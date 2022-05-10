import lzma
lzma.LZMADecompressor()

"""
zipfile.ZipFile()
tarfile.TarFile()
gzip.GzipFile()
bz2.BZ2Decompressor()
lzma.LZMADecompressor()
"""

import re
s = "hello world,world test"
s.count("world")
re.findall("world",s)
re.findall("world",s)[0]
re.split("world",s)
