import bz2
# Test BZ2Decompressor
# with open('data/data.json.bz2', 'rb') as f:
with bz2.open('data/data.json.bz2', 'rb') as f:
    for line in f:
        print(line)
# Test BZ2File
with bz2.BZ2File('data/data.json.bz2', 'rb') as f:
    for line in f:
        print(line)
 
# Test BZ2File with context manager
with bz2.BZ2File('data/data.json.bz2', 'rb') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

# Test BZ2File readlines
with bz2.BZ2File('data/data.json.bz2', 'rb') as f:
    print(f.readlines())
# Test BZ2File read()
with bz2.BZ2File('data/data.json.bz2', 'rb') as f:
    print
