import bz2
# Test BZ2Decompressor
decompressor = BZ2Decompressor()

with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

# Test BZ2File
with bz2.BZ2File('sample.bz2', 'rb') as f:
    for line in f:
        print(line)
