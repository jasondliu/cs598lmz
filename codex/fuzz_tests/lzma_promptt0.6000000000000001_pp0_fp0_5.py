import lzma
# Test LZMADecompressor
with open('lzma.txt', 'rb') as f:
    with lzma.open(f, mode='rt') as decomp:
        print(decomp.read())

# Test LZMAEncoder
with open('lzma.txt', 'rt') as f:
    with lzma.open(f, mode='wt') as enc:
        enc.write('This is a test')

# Test LZMADecompressor
with open('lzma.txt', 'rb') as f:
    with lzma.open(f, mode='rt') as decomp:
        print(decomp.read())

# Test LZMAEncoder
with open('lzma.txt', 'rt') as f:
    with lzma.open(f, mode='wt', encoding='utf-8') as enc:
        enc.write('This is a test')

# Test LZMADecompressor
with open('lzma.txt', 'rb') as f:
    with lzma.open(f, mode='rt', encoding='utf
