import bz2
bz2.BZ2File(path).read().decode('utf-8')

# or
with bz2.open(path, 'rt') as f:
    data = f.read()

# or
import bz2
with open(path, 'rb') as f:
    data = bz2.decompress(f.read()).decode('utf-8')

# or
import gzip
with gzip.open(path, 'rt') as f:
    data = f.read()

import io
import bz2
f = bz2.BZ2File(path)
data = f.read().decode('utf-8')

# or
import bz2
with bz2.BZ2File(path) as f:
    data = f.read().decode('utf-8')

# or
import bz2
with bz2.open(path, 'rt') as f:
    data = f.read()

# or
import bz2
with open(path, 'rb') as f:
    data
