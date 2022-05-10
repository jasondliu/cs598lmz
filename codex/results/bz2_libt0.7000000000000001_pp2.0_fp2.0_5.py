import bz2
bz2_file = bz2.BZ2File('data/file.bz2')

# 10.2.2 gzip
import gzip
gz_file = gzip.open('data/file.gz', 'wt')
gz_file.write('Contents go here.')
gz_file.close()

import gzip
gz_file = gzip.open('data/file.gz', 'rt')
print(gz_file.read())
gz_file.close()

# 10.2.3 lzma
import lzma
lzma_file = lzma.open('data/file.xz', 'wt')
lzma_file.write('Contents go here.')
lzma_file.close()

import lzma
lzma_file = lzma.open('data/file.xz', 'rt')
print(lzma_file.read())
lzma_file.close()

# 10.2.4 zipfile
import zipfile
with zipfile.ZipFile('data/file.zip', 'w') as
