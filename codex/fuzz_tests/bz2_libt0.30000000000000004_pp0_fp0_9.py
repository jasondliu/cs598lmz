import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rt')

# lzma
import lzma
lzma.open(filename)

# tarfile
import tarfile
tar = tarfile.open(filename)
tar.getnames()
for name in tar.getnames():
    f = tar.extractfile(name)
    content = f.read()
tar.close()

# zipfile
import zipfile
zip = zipfile.ZipFile(filename)
zip.namelist()
info = zip.getinfo('name')
content = zip.read('name')
zip.close()

# shutil
import shutil
shutil.make_archive('archive', 'zip', root_dir)
shutil.unpack_archive('archive.zip', 'destination', 'zip')
shutil.unpack_archive('archive.tar.gz', 'destination', 'gztar')

# tempfile
import tempfile
tempfile.mkstemp()
tempfile.mkdtemp()
f =
