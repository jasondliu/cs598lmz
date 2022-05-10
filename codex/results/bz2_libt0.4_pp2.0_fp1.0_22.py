import bz2
bz2.BZ2File(path, 'w')

# compress file
import gzip
with gzip.open(path, 'wt') as f:
    f.write(text)

# compress file
import bz2
with bz2.open(path, 'wt') as f:
    f.write(text)

# compress file
import lzma
with lzma.open(path, 'wt') as f:
    f.write(text)

# compress file
with gzip.open(path, 'wt') as f:
    f.write(text)

# compress file
with bz2.open(path, 'wt') as f:
    f.write(text)

# compress file
with lzma.open(path, 'wt') as f:
    f.write(text)

# compress file
with gzip.open(path, 'wt') as f:
    f.write(text)

# compress file
with bz2.open(path, 'wt') as f:
    f.write(text)

