from bz2 import BZ2Decompressor
BZ2Decompressor()

# Try other option
with open("pressure.bz2", 'rb') as f:
    file_content = f.read()
    decompressor = BZ2Decompressor()
    data = decompressor.decompress(file_content)
    print(data)

# Try other option
with open("pressure.bz2", 'rb') as f:
    decompressor = BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 1024), b''):
        data = decompressor.decompress(block)
        print(data)
