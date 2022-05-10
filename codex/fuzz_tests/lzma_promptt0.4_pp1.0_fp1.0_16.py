import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with decompressor.stream(f) as d:
        with open('test.txt', 'wb') as f:
            f.write(d.read())
# Test LZMACompressor

with open('test.txt', 'rb') as f:
    compressor = lzma.LZMACompressor()
    with compressor.stream(f) as c:
        with open('test.xz', 'wb') as f:
            f.write(c.read())
 
# Test LZMAFile

with lzma.open('test.xz') as f:
    with open('test.txt', 'wb') as f:
        f.write(f.read())
 
with open('test.txt', 'rb') as f:
    with lzma.open('test.xz', 'wb') as f:
        f.write(f.read())
 
# Test LZMAError

try:
