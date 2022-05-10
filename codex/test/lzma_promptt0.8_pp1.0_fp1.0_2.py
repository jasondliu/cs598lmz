import lzma
# Test LZMADecompressor by processing the output of LZMACompressor in multiple
# chunks and finish()-ing the decompressor in a different chunk.
decompressor = lzma.LZMADecompressor()
with open('example.xz', 'rb') as fh:
    fh.read(1)
    data = fh.read(65536)
    fh.read(1)
    file = fh.read(65536)
    fh.read(1)
    tail = fh.read()
