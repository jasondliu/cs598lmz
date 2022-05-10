import bz2
# Test BZ2Decompressor
with bz2.BZ2File('file.bz2', 'rb') as f:
    for line in f:
        print(line)

# Test BZ2Compressor
with open('file.txt', 'rb') as input:
    with bz2.BZ2File('file.bz2', 'wb') as output:
        output.writelines(input)

# Test BZ2File
with bz2.BZ2File('file.bz2', 'rb') as f:
    print(f.readline())

# Test BZ2File
with bz2.BZ2File('file.bz2', 'rb') as f:
    print(f.read())

# Test BZ2File
with bz2.BZ2File('file.bz2', 'rb') as f:
    print(f.read(100))

# Test BZ2File
with bz2.BZ2File('file.bz2', 'rb') as f:
    print(f.read(100).decode('
