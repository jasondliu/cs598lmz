import lzma
lzma.compress()
lzma.decompress()

# zipfile
import zipfile
import tempfile

with tempfile.NamedTemporaryFile() as t:
    with zipfile.ZipFile(t.name, 'w') as z:
        z.write('file.txt')

with zipfile.ZipFile(t.name) as z:
    z.read('file.txt')

# bz2
import bz2

bz2.compress()
bz2.decompress()

# tarfile
import tarfile
import tempfile

with tempfile.TemporaryFile() as t:
    with tarfile.open(fileobj=t, mode='w') as tar:
        tar.add('f.txt')

with tarfile.open(fileobj=t) as tar:
    tar.extractall()

# gzip
import gzip
import io

with io.BytesIO() as buf:
    with gzip.GzipFile(fileobj=buf, mode='w') as z:
        z.
