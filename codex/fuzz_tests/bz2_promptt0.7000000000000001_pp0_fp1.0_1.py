import bz2
# Test BZ2Decompressor object
decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

# Test BZ2File
with bz2.BZ2File('sample.bz2', 'r') as f:
    file_content = f.read()
    print(file_content)

# Test BZ2File with context manager (with)
with bz2.BZ2File('sample.bz2', 'r') as f:
    for line in f:
        print(line)

# Test BZ2File with context manager and readline() method
with bz2.BZ2File('sample.bz2', 'r') as f:
    print(f.readline())

# Test BZ2File with context manager and readlines() method
with bz2.BZ2File('sample.bz2', 'r') as f:
    print(f.readlines())

