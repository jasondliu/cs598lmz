import bz2
# Test BZ2Decompressor
with bz2.BZ2File('file.bz2', 'rb') as f:
    for line in f:
        print(line)

# Test BZ2Compressor
