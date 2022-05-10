from lzma import LZMADecompressor
LZMADecompressor().decompress(file)
#
# 'contig-NC_006793_3130527..3130686'
#
#
#
#
#

# gzip, the most commonly used compression program on Unix-like systems

import gzip

with gzip.open('somefile.gz', 'rt') as f:
    # text = f.read()
    text = f.readline()
    print(text)
    # 'contig-NC_006793_3130527..3130686'
    #
    #
    #


import gzip, zipfile

# with gzip.open(filename, mode='wt') as f:
#     f.write(text1)
#     f.write(text2)
#     f.write(text3)
#
#
#
with gzip.open(filename, 'rt') as f:
    for line in f:
        print(line)
        # contig-NC_006793_3130527..3130686
        # contig-NC_006793_31
