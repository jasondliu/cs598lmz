import lzma
lzma.decompress(compressed_data)

# bz2
import bz2
bz2.decompress(compressed_data)

# zlib
import zlib
zlib.decompress(compressed_data)

# zipfile
import zipfile
z = zipfile.ZipFile(io.BytesIO(compressed_data))
z.extractall(path='/tmp')

# tarfile
import tarfile
t = tarfile.open(mode='r:gz', fileobj=io.BytesIO(compressed_data))
t.extractall(path='/tmp')

# gzip
import gzip
gzip.decompress(compressed_data)

# subprocess
import subprocess
subprocess.run(['bzip2', '-d', '/tmp/archive.bz2'])

# lzma
import lzma
with lzma.open('/tmp/archive.xz') as f:
    f.read()

# bz2
import bz2
with bz2.
