import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()

with lzma.open('lzma.xz', mode='w', format=lzma.FORMAT_XZ) as f:
    f.write(b'hello world')

with lzma.open('lzma.xz', mode='r') as f:
    print(f.read())
 
# Test LZMADecompressor, with multiple calls to decompress

compressor = lzma.LZMACompressor()

with lzma.open('lzma.xz', mode='w', format=lzma.FORMAT_XZ) as f:
    f.write(b'hello world')

with lzma.open('lzma.xz', mode='r') as f:
    d = lzma.LZMADecompressor()
    data = f.read(1)
