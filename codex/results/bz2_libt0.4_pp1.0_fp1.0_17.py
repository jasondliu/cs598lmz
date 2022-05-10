import bz2
bz2.BZ2File(fname).read()

# uncompress
import gzip
gzip.open(fname, 'rb').read()

# uncompress
import lzma
lzma.open(fname).read()

# uncompress
import zipfile
zf = zipfile.ZipFile(fname)
zf.open(zf.namelist()[0]).read()

# uncompress
import tarfile
tf = tarfile.open(fname)
tf.extractall()

# uncompress
import bz2
bz2.BZ2File(fname).read()

# uncompress
import gzip
gzip.open(fname, 'rb').read()

# uncompress
import lzma
lzma.open(fname).read()

# uncompress
import zipfile
zf = zipfile.ZipFile(fname)
zf.open(zf.namelist()[0]).read()

# uncompress
import tarfile
tf = tarfile.open(fname)
tf.ext
