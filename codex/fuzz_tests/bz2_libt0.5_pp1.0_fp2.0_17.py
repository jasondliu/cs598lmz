import bz2
bz2.decompress(bz2_data)

# Gzip
import gzip
with gzip.open('example.txt.gz', 'rb') as f:
    file_content = f.read()

# Compress
with gzip.open('example.txt.gz', 'wb') as f:
    f.write(b"Hello, World!")

import gzip
import shutil
with open('example.txt', 'rb') as f_in:
    with gzip.open('example.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

import gzip
with gzip.open('example.txt.gz', 'rb') as f:
    file_content = f.read()

# bzip2
import bz2
with bz2.open('example.txt.bz2', 'rb') as f:
    file_content = f.read()

import bz2
import shutil
with open('example.txt', 'rb') as f_in:
   
