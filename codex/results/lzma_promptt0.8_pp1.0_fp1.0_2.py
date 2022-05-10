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
more = decompressor.decompress(data)
more += decompressor.decompress(file)
more += decompressor.decompress(tail)
more += decompressor.flush()
# Test LZMADecompressor by roughly simulating the notification that an
# incrementally decoded file is done being written.
decompressor = lzma.LZMADecompressor()
with open('example.xz', 'rb') as fh:
    while True:
        buf = fh.read(1024)
        if not buf:
            break
        data
