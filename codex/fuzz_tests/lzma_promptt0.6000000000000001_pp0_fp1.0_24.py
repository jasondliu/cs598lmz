import lzma
# Test LZMADecompressor
with open('../data/alice29.txt.xz', 'rb') as f:
    with lzma.open(f, mode='rt') as xz_file:
        text = xz_file.read()
    print(text[0:50])

with open('../data/alice29.txt.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    file_content = f.read()
    text = decompressor.decompress(file_content)
    print(text[0:50])

# Test LZMAFile
with lzma.open('../data/alice29.txt.xz', mode='rt') as xz_file:
    text = xz_file.read()
    print(text[0:50])

# Test LZMAFile
with lzma.open('../data/alice29.txt.xz', mode='rt') as xz_file:
    for line in xz_file:
        print(line, end='')
