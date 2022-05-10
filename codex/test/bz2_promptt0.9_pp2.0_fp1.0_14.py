import bz2
# Test BZ2Decompressor with the whole-file API:
d = bz2.BZ2Decompressor()
with open('lorem.bz2', 'rb') as input:
    with open('lorem_copy.txt', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(d.decompress(block))

# Test BZ2Compressor with the incremental API:
t = 'Hello, World!'
t * 128
t * 32768
t * 1000000
