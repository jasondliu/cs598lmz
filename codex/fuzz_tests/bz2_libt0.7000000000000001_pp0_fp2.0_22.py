import bz2
bz2.decompress(data)

# === gzip ===
import gzip
with gzip.open('filename.gz') as f:
    contents = f.read()

# === lzma ===
import lzma
with lzma.open('filename.xz') as f:
    contents = f.read()

# === zipfile ===
import zipfile
with zipfile.ZipFile('filename.zip') as zf:
    print(zf.namelist())
    zf.extractall()
    zf.extract('filename.txt')

# === tarfile ===
import tarfile
with tarfile.open('filename.tar') as tf:
    print(tf.namelist())
    tf.extractall()
    tf.extract('filename.txt')

# === tarfile ===
import tarfile
with tarfile.open('filename.tar') as tf:
    print(tf.namelist())
    tf.extractall()
    tf.extract('filename.txt')

# === tempfile ===
import tempfile
with temp
