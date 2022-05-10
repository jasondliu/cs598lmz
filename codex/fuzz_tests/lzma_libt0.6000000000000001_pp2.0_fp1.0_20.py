import lzma
lzma.compress('Hello world', preset=9)

lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3u\x1c', format=lzma.FORMAT_RAW, memlimit=None, filters=None)

lzma.LZMACompressor()

lzma.LZMADecompressor()

lzma.open('/tmp/foo.xz', 'wt', encoding='utf-8', errors='strict')

lzma.open('/tmp/foo.xz', 'rt')

lzma.open('/tmp/foo.xz', 'wt', mode='b')

lzma.open('/tmp/foo.xz', 'rt', mode='b')

lzma.open('/tmp/foo.xz', 'wt', mode='b', buffering=0)
