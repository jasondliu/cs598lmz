import bz2
bz2.BZ2File(filename).read()

import lzma
lzma.open(filename).read()

import zipfile
zipfile.ZipFile(filename).read()
