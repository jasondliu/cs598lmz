import lzma
# Test LZMADecompressor on bytes

comp = lzma.LZMADecompressor()
comp.decompress(b'Y2hlY2sK')

# check()
# Test LZMADecompressor on bytearray

comp = lzma.LZMADecompressor()
comp.decompress(bytearray(b'Y2hlY2sK'))

# check()
# Test LZMADecompressor on list of bytes

comp = lzma.LZMADecompressor()
comp.decompress([b'Y', b'2', b'h', b'l', b'Y', b'2', b's', b'K'])

# check()
# Test LZMADecompressor on generators of bytes

def gen():
    for b in [b'Y', b'2', b'h', b'l', b'Y', b'2', b's', b'K']:
        yield b

comp = lzma.LZMADecompressor()
comp.decompress
