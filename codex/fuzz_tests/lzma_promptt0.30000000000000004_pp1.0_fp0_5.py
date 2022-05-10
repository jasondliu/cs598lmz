import lzma
# Test LZMADecompressor
with open('data/enwik9.txt.xz', 'rb') as f:
    with lzma.open(f, 'rb') as xf:
        file_content = xf.read()
        print(len(file_content))

# Test LZMACompressor
with open('data/enwik9.txt', 'rb') as f:
    with lzma.open('data/enwik9.txt.xz', 'wb') as xf:
        xf.write(f.read())

# Test LZMAFile
with lzma.open('data/enwik9.txt.xz', 'rb') as xf:
    file_content = xf.read()
    print(len(file_content))

# Test LZMAFile
with open('data/enwik9.txt.xz', 'rb') as f:
    with lzma.LZMAFile(f, 'rb') as xf:
        file_content = xf.read()
        print(len(file_content))

# Test L
