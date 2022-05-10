import bz2
bz2_f = bz2.BZ2File('/Users/gmccarthy/big_file.bz2')
bz2_f.readlines()
bz2_f.close()

with bz2.BZ2File('/Users/gmccarthy/big_file.bz2') as f:
    contents = f.readlines()
    print contents

import gzip
with gzip.open('/Users/gmccarthy/big_file.bz2', 'rb') as f:
    contents = f.readlines()

with gzip.open('/Users/gmccarthy/big_file.bz2') as in_f:
    with open('/Users/gmccarthy/big_file.txt', 'wb') as out_f:
        for line in in_f:
            out_f.write(line)


def yield_from_file(filename) : 
    with open(filename) as f:
        for line in f:
            yield line
for line in yield_from_file('/Users/gmccarthy/
