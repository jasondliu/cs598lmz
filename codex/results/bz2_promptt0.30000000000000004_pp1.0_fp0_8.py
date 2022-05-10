import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open('data.bz2', 'rb') as f:
    file_content = f.read()
    data = decompressor.decompress(file_content)
    print(data)

# Test BZ2File
with bz2.BZ2File('data.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)

# Test BZ2File with context manager
with bz2.BZ2File('data.bz2', 'rb') as f:
    for line in f:
        print(line)

# Test BZ2File with context manager and readline
with bz2.BZ2File('data.bz2', 'rb') as f:
    print(f.readline())

# Test BZ2File with context manager and readlines
with bz2.BZ2File('data.bz2', 'rb') as f:
    print(f.readlines())

# Test
