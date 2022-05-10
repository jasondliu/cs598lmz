import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data.bz2', 'rb') as input:
    with open('data.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

print(output.tell())

# Test BZ2File

with bz2.open('data.bz2', 'rb') as input:
    with open('data2.txt', 'wb') as output:
        while True:
            block = input.read(100 * 1024)
            if not block:
                break
            output.write(block)

print(output.tell())

# Test BZ2File with context manager

with bz2.open('data.bz2', 'rb') as input, \
     open('data3.txt', 'wb') as output:
    while True:
        block = input.read(100 * 1024)
        if not block:
            break
       
