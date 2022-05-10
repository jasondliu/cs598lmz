from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed)

import gzip
import io
buf = io.BytesIO()
with gzip.GzipFile(fileobj=buf, mode='w') as f:
    f.write(data)
buf.getvalue()
with gzip.GzipFile(fileobj=buf, mode='r') as f:
    f.read(1024)
 
# With context manager
with gzip.open('file.gz', mode='wt') as f:
    f.write(text)
with gzip.open('file.gz', mode='rt') as f:
    text = f.read()

with open('file.gz', 'rb') as f_in, gzip.open('file.gz', 'wb') as f_out:
    f_out.writelines(f_in)

# Reading line by line
import gzip
with gzip.open('file.gz', mode='rt') as f:
    for line in f:
        print(line)

# Random access
import gzip
import shutil

with open('somefile
