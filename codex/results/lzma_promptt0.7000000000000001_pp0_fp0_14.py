import lzma
# Test LZMADecompressor
with lzma.open("/Users/szabolcs/dev/github/pandas/pandas/tests/data/test1.xz", "r") as f:
    print(f.read())

import lzma
# Test LZMACompressor
with lzma.open("/Users/szabolcs/dev/github/pandas/pandas/tests/data/test2.xz", "w") as f:
    f.write("Hello world!")
    f.flush()

import lzma
# Test LZMADecompressor.copy
with lzma.open("/Users/szabolcs/dev/github/pandas/pandas/tests/data/test1.xz", "r") as source:
    with lzma.open("/Users/szabolcs/dev/github/pandas/pandas/tests/data/test2.xz", "w") as target:
        target.write(source.read())
        target.flush()

import lzma

