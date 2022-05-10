import bz2
bz2.BZ2File(filename, 'w')

# open a gzip-compressed file
import gzip
gzip.open(filename, 'wt')

# open a bz2-compressed file
import bz2
bz2.open(filename, 'wt')

# read the first four bytes of a gzip-compressed file
import gzip
with gzip.open('file.gz', 'rb') as f:
    print(f.read(4))

# write compressed data to a buffer
import gzip
buf = io.BytesIO()
with gzip.GzipFile(fileobj=buf, mode='w') as f:
    f.write(b'hello world')

# read a gzip-compressed file
import gzip
with gzip.open('file.gz', 'rt') as f:
    text = f.read()

# write text data to a gzip-compressed file
import gzip
with gzip.open('file.gz', 'wt') as f:
    f.write(text)

# read a g
