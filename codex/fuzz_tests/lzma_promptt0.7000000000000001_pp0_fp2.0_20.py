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

with open('lorem.txt', 'rb') as fr:
    f_in = fr.read()
    f_out = comp.compress(f_in)
    f_out += comp.flush()
    f_in2 = uncomp.decompress(f_out)
    f_in == f_in2

with lzma.open('foo.lzma', 'rb') as fr:
    data = fr.read()
with lzma.open('foo.xz', 'wb') as fw:
    f
