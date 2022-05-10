import lzma
# Test LZMADecompressor
with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(10)
    while data:
        print(decompressor.decompress(data))
        data = f.read(10)

# Test LZMAFile
with lzma.open('test.xz') as f:
    print(f.read())

# Test LZMAFile with mode='w'
with lzma.open('test.xz', mode='w') as f:
    f.write(b'hello world\n')

# Test LZMAFile with mode='r'
with lzma.open('test.xz', mode='r') as f:
    print(f.read())

# Test LZMAFile with mode='a'
with lzma.open('test.xz', mode='a') as f:
    f.write(b'hello world\n')

# Test LZMAFile with mode='x'
try:
    lz
