import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('data/smaller.txt.bz2', 'rb') as f:
    next_chunk = f.read(100)
    while next_chunk:
        print(decompressor.decompress(next_chunk))
        next_chunk = f.read(100)

# Test BZ2File
with bz2.BZ2File('data/smaller.txt.bz2', 'rb') as f:
    print(f.read())

# Compress
with open('data/smaller.txt', 'rb') as rf:
    with bz2.BZ2File('data/smaller.txt.bz2', 'wb') as wf:
        wf.write(rf.read())
 
# Decompress
with open('data/smaller.txt', 'wb') as wf:
    with bz2.BZ2File('data/smaller.txt.bz2', 'rb') as rf:
        wf.
