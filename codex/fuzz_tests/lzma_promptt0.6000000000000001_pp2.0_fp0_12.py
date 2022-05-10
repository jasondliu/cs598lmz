import lzma
# Test LZMADecompressor
with open('/tmp/test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with open('/tmp/test.txt', 'wb') as f2:
        for buf in iter(lambda: f.read(1024 * 1024), b''):
            f2.write(decompressor.decompress(buf))
        f2.write(decompressor.flush())

import lzma
# Test LZMADecompressor
with open('/tmp/test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with open('/tmp/test.txt', 'wb') as f2:
        f2.write(decompressor.decompress(f.read()))

import lzma
# Test LZMADecompressor
with open('/tmp/test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with open('/tmp/test.txt
