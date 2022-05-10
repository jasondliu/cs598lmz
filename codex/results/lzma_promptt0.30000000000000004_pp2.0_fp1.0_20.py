import lzma
# Test LZMADecompressor

# NOTE: This test is not exhaustive, but it does test the basic
# functionality of the LZMADecompressor class.

# Test the decompressor on a file created with the xz command line tool
with open("testdata/lzma_compat.xz", "rb") as f:
    xz_file = f.read()

# Test the decompressor on a file created with the lzma command line tool
with open("testdata/lzma_compat.lzma", "rb") as f:
    lzma_file = f.read()

# Test the decompressor on a file created with the lzma command line tool
# using the --format=lzma option
with open("testdata/lzma_compat.alone", "rb") as f:
    alone_file = f.read()

# Test the decompressor on a file created with the lzma command line tool
# using the --format=alone option
with open("testdata/lzma_compat.raw", "rb") as f:
    raw_file =
