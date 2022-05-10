import bz2
# Test BZ2Decompressor

# Test decompress()
decompressor = bz2.BZ2Decompressor()

with open('lorem.txt.bz2', 'rb') as input:
    with open('lorem_copy.txt', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(decompressor.decompress(block))

# Test decompress() with max_length
decompressor = bz2.BZ2Decompressor()

with open('lorem.txt.bz2', 'rb') as input:
    with open('lorem_copy.txt', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(decompressor.decompress(block, 1024))

# Test decompress() with max_length and unconsumed_tail
decompressor = bz2.BZ2Decompressor()

with open('lorem.txt.bz2', 'rb
