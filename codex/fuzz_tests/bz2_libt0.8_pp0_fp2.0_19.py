import bz2
bz2_file = bz2.open('corpus.txt.bz2', 'wt')
bz2_file.write(all_text)
bz2_file.close()
print('bz2 compression:', os.stat('corpus.txt.bz2').st_size / len(all_text))

import lzma
lzma_file = lzma.open('corpus.txt.xz', 'wt')
lzma_file.write(all_text)
lzma_file.close()
print('xz compression:', os.stat('corpus.txt.xz').st_size / len(all_text))

import gzip
gzip_file = gzip.open('corpus.txt.gz', 'wt')
gzip_file.write(all_text)
gzip_file.close()
print('gzip compression:', os.stat('corpus.txt.gz').st_size / len(all_text))

from lzma import LZMAFile, XZFile
with
