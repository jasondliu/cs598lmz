import bz2
bz2.decompress(bz2.compress(b'hello world'))

import gzip
with gzip.open('/tmp/file.gz', 'wt') as f:
    f.write('hello world')

with gzip.open('/tmp/file.gz', 'rt') as f:
    text = f.read()

import zipfile
with zipfile.ZipFile('/tmp/file.zip', 'w') as zf:
    zf.write('/tmp/file.gz')

with zipfile.ZipFile('/tmp/file.zip', 'r') as zf:
    with zf.open('file.gz') as f:
        text = f.read()

import shutil
shutil.unpack_archive('/tmp/file.zip', '/tmp/outdir')

shutil.make_archive('/tmp/archive', 'zip', '/tmp/outdir')

shutil.get_archive_formats()

import tempfile
with tempfile.TemporaryFile(mode='w+t') as f:
   
