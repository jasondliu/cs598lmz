import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    file_content = f.read()
    print(len(file_content))
    unc = decompressor.decompress(file_content)
    print(len(unc))

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2') as f:
    file_content = f.read()
    print(len(file_content))

# Test BZ2File with context manager

with bz2.BZ2File('data/enwik8.bz2') as f:
    for i in range(10):
        print(f.readline())

# Test BZ2File with context manager

with bz2.BZ2File('data/enwik8.bz2') as f:
    for i in range(10):
        print(f.readline().decode('utf-8'))

# Test BZ
