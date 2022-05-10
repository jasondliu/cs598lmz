import bz2
# Test BZ2Decompressor

with open('enwik8', 'rb') as f:
    with bz2.BZ2Decompressor() as decompressor:
        while True:
            block = f.read(1024)
            if not block:
                break
            decompressed = decompressor.decompress(block)
            if decompressed:
                print(decompressed)
                break

print('-' * 50)

# Test BZ2File

with bz2.BZ2File('enwik8', 'rb') as f:
    for line in f:
        print(line)
        break

print('-' * 50)

# Test BZ2Compressor

with open('enwik8', 'rb') as f:
    with bz2.BZ2Compressor(9) as compressor:
        while True:
            block = f.read(1024)
            if not block:
                break
            compressed = compressor.compress(block)
            if compressed:
                print(compressed)
                break

print('-' * 50)

# Test BZ
