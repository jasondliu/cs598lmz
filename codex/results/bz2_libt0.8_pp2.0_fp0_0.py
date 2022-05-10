import bz2
bz2.BZ2File('bz2file.txt.bz2', 'w')

# ZIP
import zipfile
zipfile.is_zipfile('file.zip')
zipfile.ZipFile('file.zip', 'w')
zfile = zipfile.ZipFile('file.zip', 'a')
zfile.write('file.txt', 'file_in_archive.txt')
zfile.writestr('file_in_archive.txt', 'Hello, World!')
zfile.close()
zfile = zipfile.ZipFile('file.zip', 'r')
zfile.namelist()
zfile.read('file_in_archive.txt')
zfile.extract('file_in_archive.txt')
zfile.extractall()
zfile.close()

# BZIP2
import bz2
bz2.BZ2File('bz2file.txt.bz2', 'w')

# GZIP
import gzip
gzip.GzipFile('gzipfile.txt.gz', 'w')

# T
