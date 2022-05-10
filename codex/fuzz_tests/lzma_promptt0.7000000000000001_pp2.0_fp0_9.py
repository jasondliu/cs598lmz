import lzma
# Test LZMADecompressor:
with open('data/lzmatest.xz', 'rb') as input, lzma.open(input) as uncomp:
    print(uncomp.read())

# Test LZMACompressor:
with lzma.open('data/lzmatest.xz', mode='wt') as comp:
    comp.write('The quick brown fox jumps over the lazy dog')

with open('data/lzmatest.xz', 'rb') as input, lzma.open(input) as uncomp:
    print(uncomp.read())

# Test LZMAFile:
with lzma.open('data/lzmatest.lzma', 'wt') as comp:
    comp.write('The quick brown fox jumps over the lazy dog')

with lzma.open('data/lzmatest.lzma') as uncomp:
    print(uncomp.read())

# Test LZMAFile (with options):
with lzma.open('data/lzmatest.lzma', preset=9 | lzma.PRESET
