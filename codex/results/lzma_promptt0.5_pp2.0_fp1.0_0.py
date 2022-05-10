import lzma
# Test LZMADecompressor
with lzma.open('data/python.xz') as input:
    with open('data/python.out', 'wb') as output:
        while True:
            try:
                output.write(input.read(1024))
            except EOFError:
                break


# Example: Compressing Data
import bz2
data = open('data/lorem.txt', 'rb').read()
len(data)

compressed = bz2.compress(data)
len(compressed)

decompressed = bz2.decompress(compressed)
len(decompressed)

decompressed == data


# Example: Using a Compression File
import bz2
with bz2.open('data/lorem.bz2', 'wt') as output:
    output.write('The same line, over and over.\n')

with bz2.open('data/lorem.bz2', 'rt') as input:
    print(input.read())


# Example: Using a Compression File with Data Compression Levels
for
