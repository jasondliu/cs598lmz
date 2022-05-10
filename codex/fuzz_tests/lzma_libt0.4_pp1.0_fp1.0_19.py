import lzma
lzma.LZMAFile(open('/home/jovyan/data/bulk/bulk-downloads/2017/2017-12-20/2017-12-20.tar.xz', 'rb'))

#!/usr/bin/env python

import lzma
import os
import sys
import tarfile

if len(sys.argv) != 2:
    print("Usage: python3 extract.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with lzma.LZMAFile(filename) as f:
    with tarfile.open(fileobj=f) as tar:
        tar.extractall()

os.rename(os.path.splitext(filename)[0], "data")

import os
import sys
import tarfile

if len(sys.argv) != 2:
    print("Usage: python3 extract.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with tarfile.open(filename) as
