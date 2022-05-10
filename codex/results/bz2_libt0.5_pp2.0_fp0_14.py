import bz2
bz2.BZ2File(file_name)

# zip
import zipfile
zipfile.ZipFile(file_name)

# gzip
import gzip
gzip.GzipFile(file_name)

import lzma
lzma.LZMAFile(file_name)

# tar
import tarfile
tarfile.TarFile(file_name)
