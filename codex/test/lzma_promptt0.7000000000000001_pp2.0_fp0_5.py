import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
with lzma.open('foo.lzma', mode = 'wt') as f:
    f.write('hello world\n')

with open('foo.lzma', 'rb') as f:
    file_content = f.read()

print(compressor.decompress(file_content))
