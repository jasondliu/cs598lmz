import bz2
# Test BZ2Decompressor
with bz2.BZ2File('data/sample.bz2', 'r') as f:
    print(f.readline())

with bz2.BZ2File('data/sample.bz2', 'r') as f:
    print(f.readlines())

with bz2.BZ2File('data/sample.bz2', 'r') as f:
    print(f.read())

with bz2.BZ2File('data/sample.bz2', 'r') as f:
    for line in f:
        print(line)

with bz2.BZ2File('data/sample.bz2', 'r') as f:
    print(f.read(10))

with bz2.BZ2File('data/sample.bz2', 'r') as f:
    print(f.read(10))

with bz2.BZ2File('data/sample.bz2', 'r') as f:
    print(f.read(10))

with bz2
