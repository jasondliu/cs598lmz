import bz2
bz2.BZ2Compressor()
# ...
bz2.BZ2Decompressor()
# ...

# Rarfile
# pip install rarfile
import rarfile
rarfile.RarFile('file.rar')
# ...

# Zipfile
# pip install zipfile
import zipfile
zipfile.ZipFile('file.zip')
# ...

# Tarfile
# pip install tarfile
import tarfile
tarfile.TarFile('file.tar')
# ...

# Gzipfile
# pip install gzipfile
import gzipfile
gzipfile.GzipFile('file.gz')
# ...

# Bz2file
# pip install bz2file
import bz2file
bz2file.BZ2File('file.bz2')
# ...

# Compile PyPy
# sudo apt-get install build-essential libffi-dev libssl-dev
# sudo apt-get install pypy pypy-dev
# cd pypy-6.0.0-src
# make -j 4
# pip
