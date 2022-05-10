import bz2
bz2.BZ2File

import gzip
gzip.open

with open("data.txt", "rt") as f:
    data = f.read()
