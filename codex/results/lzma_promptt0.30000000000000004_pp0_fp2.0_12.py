import lzma
# Test LZMADecompressor

# Test basic functionality

with open('lzma_compat.py', 'rb') as f:
    with lzma.open(f, 'r') as f2:
        data = f2.read()

with open('lzma_compat.py', 'rb') as f:
    with lzma.open(f, 'r') as f2:
        data2 = f2.read()

assert data == data2

with open('lzma_compat.py', 'rb') as f:
    with lzma.open(f, 'r') as f2:
        data = f2.read(100)
        data += f2.read(100)
        data += f2.read()

with open('lzma_compat.py', 'rb') as f:
    with lzma.open(f, 'r') as f2:
        data2 = f2.read(100)
        data2 += f2.read(100)
        data2 += f2.read()

assert data == data2
