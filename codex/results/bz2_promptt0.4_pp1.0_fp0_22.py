import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik9.bz2', 'rb') as f:
    data = f.read(100)
    while True:
        decompressed = decompressor.decompress(data)
        if decompressed:
            print(decompressed)
            break
        else:
            data = f.read(100)
            if not data:
                break

print('-' * 20)

# Test BZ2File

with bz2.BZ2File('data/enwik9.bz2', 'rb') as f:
    for line in f:
        print(line)
        break

print('-' * 20)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

data = b'hello world'
compressed = compressor.compress(data)
print(compressed)

compressed = compressor.flush()
print(compressed)

print('-' * 20)

# Test BZ2File
