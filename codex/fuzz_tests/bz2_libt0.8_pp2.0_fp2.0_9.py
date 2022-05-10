import bz2
bz2.decompress(bz2_data)
result

!bunzip2 -k testfile.bz2

!cat testfile

!bzip2 -k testfile
!ls -l 
!bunzip2 -k testfile.bz2

## Compression with gzip

with gzip.open('testfile2.gz', 'wt') as output:
    output.write(textdata)
with gzip.open('testfile2.gz', 'rt') as input:
    print(input.read())

!cat testfile2.gz

!gzip -d testfile2.gz
!cat testfile2

!gzip -k testfile
!ls -l 
!gzip -d testfile.gz

!wget https://github.com/pydata/pydata-book/blob/2nd-edition/datasets/alice.txt.gz?raw=true -O alice.txt.gz

!ls -l alice.txt.gz

import gzip
import shutil
with g
