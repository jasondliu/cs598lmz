from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#bz2
import bz2
bz2.decompress(data)

#zlib
import zlib
zlib.decompress(data)

#gzip
import gzip
gzip.decompress(data)

#tarfile
import tarfile
tarfile.is_tarfile('sample.tar.gz')

#tarfile
import tarfile
tar = tarfile.open('sample.tar.gz', 'r')
tar.extractall()
tar.close()

#tarfile
import tarfile
tar = tarfile.open('sample.tar.gz', 'r:gz')
tar.extractall()
tar.close()

#tarfile
import tarfile
tar = tarfile.open('sample.tar.gz', 'r:bz2')
tar.extractall()
tar.close()

#tarfile
import tarfile
tar = tarfile.open('sample.tar.gz', 'r:xz')
tar.extractall()
tar.close()

#tar
