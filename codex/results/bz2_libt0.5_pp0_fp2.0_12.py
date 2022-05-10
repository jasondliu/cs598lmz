import bz2
bz2.decompress(compressed).decode('utf-8')

# bz2.open()
# bz2.open()
# bz2.open()

with bz2.open('file.bz2', 'wt') as f:
    f.write(text)

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())


# gzip

import gzip
s = gzip.compress(b'witch which has which witches wrist watch')
print(len(s))

t = gzip.decompress(s)
print(t)

with gzip.open('file.gz', 'wt') as f:
    f.write(text)

with gzip.open('file.gz', 'rt') as f:
    print(f.read())

with gzip.open('file.gz', 'rb') as f:
    print(f.read())


# zipfile

import zipfile
with zipfile.ZipFile('file.zip', 'w')
