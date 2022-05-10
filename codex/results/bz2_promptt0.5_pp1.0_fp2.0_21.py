import bz2
# Test BZ2Decompressor on a small chunk of data
with open('data/example.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    chunk = f.read(30)
    print(decompressor.decompress(chunk))

# Read the entire file using a bigger chunk size
with open('data/example.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for chunk in iter(lambda: f.read(100 * 1024), b''):
        print(decompressor.decompress(chunk))

# Read the entire file using a bigger chunk size
with open('data/example.bz2', 'rb') as f:
    data = bz2.decompress(f.read())
    print(data)

# Read the entire file using a bigger chunk size
with bz2.open('data/example.bz2', 'rb') as f:
    data = f.read()
    print(data)

# Read the entire file using a bigger
