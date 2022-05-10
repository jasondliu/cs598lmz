import bz2
# Test BZ2Decompressor on a single file

# Open the file and read the first 10 characters
with bz2.open('../data/sample.json.bz2', 'rb') as f:
    print(f.read(10))
# Open the file and decompress the first 10 characters
with bz2.open('../data/sample.json.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    print(decompressor.decompress(f.read(10)))
# Open the file and decompress the first 10 characters
with bz2.open('../data/sample.json.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    print(decompressor.decompress(f.read(10)))
# Open the file and decompress the first 10 characters
with bz2.open('../data/sample.json.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    print(decompressor.decomp
