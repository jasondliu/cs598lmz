import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

import gzip
with gzip.open('test.gz', 'wt') as f:
    f.write('Hello World!')
with gzip.open('test.gz', 'rt') as f:
    print(f.read())

import zipfile
with zipfile.ZipFile('test.zip', 'w') as zf:
    zf.write('test.gz')
with zipfile.ZipFile('test.zip', 'r') as zf:
    print(zf.namelist())
    with zf.open('test.gz') as f:
        print(f.read())

from io import BytesIO
import tarfile
with tarfile.open('test.tar', 'w') as tf:
    tf.add('test.gz')
with tarfile.open('test.tar', 'r') as tf:
    print(tf.getnames())
    with tf.extractfile('test.gz') as f:
        print(f.read())

with tar
