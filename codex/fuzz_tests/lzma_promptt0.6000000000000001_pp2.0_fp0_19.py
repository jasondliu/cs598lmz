import lzma
# Test LZMADecompressor

import lzma
import os
import sys

decomp = lzma.LZMADecompressor()

with open(sys.argv[1], 'rb') as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        data = decomp.decompress(chunk)
        if data:
            sys.stdout.write(data)
    sys.stdout.write(decomp.flush())
