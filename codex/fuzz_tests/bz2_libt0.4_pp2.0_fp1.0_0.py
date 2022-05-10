import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rt')

# lzma
import lzma
lzma.open(filename)

# zipfile
import zipfile
zf = zipfile.ZipFile(filename)
zf.extractall(path='/tmp/')
zf.close()

# tarfile
import tarfile
tf = tarfile.open(filename)
tf.extractall(path='/tmp/')
tf.close()

# send2trash
import send2trash
send2trash.send2trash(filename)

# shutil
import shutil
shutil.copy(filename, '/tmp/')
shutil.copytree(dirname, '/tmp/')
shutil.move(filename, '/tmp/')
shutil.rmtree(dirname)

# tempfile
import tempfile
tempfile.TemporaryFile()
tempfile.NamedTemporaryFile()
tempfile.TemporaryDirectory()

# glob
import glob
gl
