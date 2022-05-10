import bz2
# Test BZ2Decompressor

# Read and decompress some data
decompressor = bz2.BZ2Decompressor()

with open('lorem.txt.bz2', 'rb') as input:
    while True:
        block = input.read(1024)
        if not block:
            break
        print(decompressor.decompress(block))

