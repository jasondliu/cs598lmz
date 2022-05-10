import lzma
# Test LZMADecompressor

comp = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    data = f.read()
    print(comp.decompress(data))

with open('test.xz', 'rb') as f:
    data = f.read()
    print(comp.decompress(data))

with open('test.xz', 'rb') as f:
    data = f.read()
    print(comp.decompress(data))

with open('test.xz', 'rb') as f:
    data = f.read()
    print(comp.decompress(data))

with open('test.xz', 'rb') as f:
    data = f.read()
    print(comp.decompress(data))

with open('test.xz', 'rb') as f:
    data = f.read()
    print(comp.decompress(data))

with open('test.xz', 'rb') as f:
    data = f.read()
