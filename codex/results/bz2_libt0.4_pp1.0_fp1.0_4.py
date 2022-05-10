import bz2
bz2.BZ2File(filename).read()

# gzip
import gzip
gzip.open(filename).read()

# gzip
with gzip.open(filename, 'wt') as f:
    f.write(text)

with gzip.open(filename, 'rt') as f:
    text = f.read()

# bz2
import bz2
with bz2.open(filename, 'wt') as f:
    f.write(text)

with bz2.open(filename, 'rt') as f:
    text = f.read()

# lzma
import lzma
with lzma.open(filename, 'wt') as f:
    f.write(text)

with lzma.open(filename, 'rt') as f:
    text = f.read()

# tar
import tarfile
with tarfile.open(filename) as f:
    f.extractall()

with tarfile.open(filename, 'w:gz') as f:
    f.add('filename')
