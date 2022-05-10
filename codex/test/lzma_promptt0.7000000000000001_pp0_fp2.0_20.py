import lzma
# Test LZMADecompressor and LZMACompressor classes

# Read from a file and write the compressed output to another file
with lzma.open('foo.xz', 'rb') as fr:
    data = fr.read()
with lzma.open('foo.lzma', 'wb') as fw:
    fw.write(data)
# Use LZMADecompressor and LZMACompressor mechanisms directly
comp = lzma.LZMACompressor()
uncomp = lzma.LZMADecompressor()

