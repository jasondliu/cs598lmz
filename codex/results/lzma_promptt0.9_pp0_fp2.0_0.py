import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
with open('testdata/alice29.txt', 'rb') as fin:
    comp = fin.read()

decomp.decompress(comp)

import lzma
# Decompress a file using LZMA
with lzma.open('testdata/alice29.txt.xz', 'rt') as fin:
    text = fin.read()

import lzma
# Compress a file using LZMA
with open('/tmp/something.txt', 'wt') as fout:
    with lzma.open('testdata/alice29.txt.xz') as fin:
        fout.write(fin.read())

import lzma

[X]=1 2 3
for x in $X
do
  time cat testdata/alice29.txt | lzma > /dev/null
done

[X]=1 2 3
for x in $X
do
  time uncompress -c testdata/alice29.txt.Z > /dev/
