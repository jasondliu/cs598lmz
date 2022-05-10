import lzma
# Test LZMADecompressor

data = lzma.compress(b"Hello World!")

decomp = lzma.LZMADecompressor()
result = decomp.decompress(data)

print(result.decode())

# Test LZMAFile

with open('lzma.txt', 'r') as f:
    data = f.read()

print(data)

decomp = lzma.LZMADecompressor()
result = decomp.decompress(data.encode())

print(result.decode())

with lzma.open('lzma.txt', 'r') as f:
    result = f.read()

print(result)

# Test CompressFile

with open('lzma.txt', 'r') as f:
    data = f.read()

with lzma.open('lzma.lz', 'w', format=lzma.FORMAT_XZ) as f:
    f.write(data.encode())

with open('lzma.lz
