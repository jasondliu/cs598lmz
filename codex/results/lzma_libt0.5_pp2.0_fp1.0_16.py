import lzma
lzma.LZMAFile

# lzma.open()

import sys
import lzma

with lzma.open(sys.argv[1]) as f:
    file_content = f.read()
    print(file_content)

import sys
import lzma

with lzma.open(sys.argv[1], mode="rt") as f:
    file_content = f.read()
    print(file_content)

# lzma.open()

import sys
import lzma

with lzma.open(sys.argv[1], mode="wt") as f:
    f.write(sys.argv[2])

# lzma.open()

import sys
import lzma

with lzma.open(sys.argv[1], mode="wt") as f:
    f.write(sys.argv[2])

with lzma.open(sys.argv[1], mode="rt") as f:
    file_content = f.read()
    print
