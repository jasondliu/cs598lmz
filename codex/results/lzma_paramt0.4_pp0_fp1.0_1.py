from lzma import LZMADecompressor
LZMADecompressor().decompress(open('/var/tmp/python-lzma-0.4.9.tar.bz2', 'rb').read())

# uncompress bzip2
import bz2
bz2.decompress(open('/var/tmp/python-lzma-0.4.9.tar.bz2', 'rb').read())

# uncompress gzip
import gzip
gzip.decompress(open('/var/tmp/python-lzma-0.4.9.tar.gz', 'rb').read())

# uncompress zip
import zipfile
z = zipfile.ZipFile('/var/tmp/python-lzma-0.4.9.zip')
z.extractall()

# uncompress tar
import tarfile
t = tarfile.open('/var/tmp/python-lzma-0.4.9.tar.gz')
t.extractall()

# uncompress lzma
import lzma
lzma.decompress(open('/var/tmp/python-
