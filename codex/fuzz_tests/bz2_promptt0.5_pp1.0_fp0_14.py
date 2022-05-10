import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
with open('data/example.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

print()

# Test BZ2File
with bz2.BZ2File('data/example.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)

print()

# Test BZ2File with context manager
with bz2.BZ2File('data/example.bz2', 'rb') as f:
    for line in f:
        print(line)

print()

# Test BZ2File with context manager
with bz2.BZ2File('data/example.bz2', 'rb') as f:
    print(f.readline())

print()

# Test BZ2File with context manager
with bz2.BZ2File('data/example.bz2', 'rb') as
