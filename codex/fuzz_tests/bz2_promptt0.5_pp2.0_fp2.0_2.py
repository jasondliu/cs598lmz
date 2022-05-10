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

print(decompressor.decompress(b''))

# Decompress a file
with open('lorem.txt.bz2', 'rb') as input:
    with open('lorem.txt', 'wt') as output:
        decompressor = bz2.BZ2Decompressor()
        for block in iter(lambda: input.read(1024), b''):
            output.write(decompressor.decompress(block))
        output.write(decompressor.flush())
 
# Compress a file
with open('lorem.txt', 'rt') as input:
    with bz2.open('lorem.txt.bz2', 'wt') as output:
        output.writelines
