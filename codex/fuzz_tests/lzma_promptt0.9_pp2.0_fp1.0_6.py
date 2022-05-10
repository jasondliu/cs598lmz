import lzma
# Test LZMADecompressor by decompressing the binary data of text.txt.xz.
with open('text.txt.xz', 'rb') as f:
    file_content = f.read()

with lzma.open('text.txt.xz') as f:
    file_content = f.read()
decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(file_content)
print(result.decode('utf-8'))
with lzma.open('text.txt.xz') as f:
    file_content = f.read()
print(f.read(10).decode('utf-8'))

lzc = lzma.LZMACompressor(check=-1)
lzd = lzma.LZMADecompressor()
data_111 = b"This is a test of how this works.\n" * 100
comp = lzc.compress(data_111)
comp += lzc.flush()
print(comp)
data_222 = lzd.decomp
