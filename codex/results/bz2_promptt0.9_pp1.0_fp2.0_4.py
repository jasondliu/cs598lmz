import bz2
# Test BZ2Decompressor class
with open('files/files_vs_io/uncompressed.bin', 'rb') as input:

    with open('files/files_vs_io/zlib.bz2', 'wb') as output:

        compressor = bz2.BZ2Compressor()

        while True:

            block = input.read(64)

            if not block:
                break

            output.write(compressor.compress(block))

        output.write(compressor.flush())
# Test BZ2Decompressor class
with open('files/files_vs_io/uncompressed.bin', mode='wb', buffering=0) as uncompressed:

    with bz2.open('files/files_vs_io/bz2.bz2', 'rb', buffering=0) as compressed:
        uncompressed.write(compressed.read())
# TextIOWrapper for reading encoded text
from io import BytesIO
import os
import fnmatch
import re
from collections import Counter

with BytesIO() as input:

    with open('files/files_vs
