import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor

with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(1)
    while data:
        print(decompressor.decompress(data))
        data = f.read(1)

# Test LZMAFile
# https://docs.python.org/3/library/lzma.html#lzma.LZMAFile

with lzma.open('test.xz') as f:
    print(f.read())

# Test LZMAError
# https://docs.python.org/3/library/lzma.html#lzma.LZMAError

try:
    lzma.open('test.xz', format=lzma.FORMAT_ALONE)
except lzma.LZMAError as e:
    print(e)

# Test LZMAError
