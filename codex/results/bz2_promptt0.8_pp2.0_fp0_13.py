import bz2
# Test BZ2Decompressor

decomp = bz2.decompressobj()
with open('texts/enwik9.txt', 'rb') as f:
    data = f.read(1000)
    data = decomp.decompress(data)

print(data.decode('utf-8'))

print(decomp.needs_input)

print(decomp.unused_data)

print(decomp.eof)

# Test BZ2Decompressor

decomp = bz2.decompressobj()
count = 0
with open('texts/enwik9.txt', 'rb') as f:
    while True:
        data = f.read(2000)
        if data:
            data = decomp.decompress(data)
            count += len(data)
        else:
            break

print(count)

# Test BZ2Decompressor

decomp = bz2.decompressobj()
count = 0
with open('texts/enwik9.txt', 'rb') as f:
    while True:
       
