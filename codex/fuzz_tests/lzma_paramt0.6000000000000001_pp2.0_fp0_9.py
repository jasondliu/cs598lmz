from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x5d\x00\x00\x80\x0e\xff\x0f\x00\x00\x00')

# decompress from stream
from lzma import LZMADecompressor
c = LZMADecompressor()
with open('lzma_compressed.xz', 'rb') as f:
    for block in iter(lambda: f.read(64 * 1024), b''):
        print(c.decompress(block))
