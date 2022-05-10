import lzma
# Test LZMADecompressor on data produced by the LZMA C example code.
# First, create a file of known data.
with open('lzma_C_example.xz', 'rb') as fh:
    data = fh.read()
with lzma.open('lzma_C_example.xz') as fh:
    fh.read()
with lzma.open('lzma_C_example.xz', format=lzma.FORMAT_ALONE) as fh:
    fh.read()
with lzma.open('lzma_C_example.xz', format=lzma.FORMAT_XZ) as fh:
    fh.read()
with lzma.open('lzma_C_example.xz', format=lzma.FORMAT_RAW) as fh:
    fh.read()
with lzma.open('lzma_C_example.xz', format=lzma.FORMAT_AUTO) as fh:
    fh.read()
with lzma
