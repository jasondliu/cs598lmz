from lzma import LZMADecompressor
LZMADecompressor.decompress(compressed_data)

# Open a file in binary read mode
with open('somefile.xz', 'rb') as input:
    with lzma.open(input) as decompressor:
        for line in decompressor:
            print(line)

# Compress a file
with open('somefile', 'rb') as input:
    with lzma.open('somefile.xz', 'w') as output:
        output.write(input.read())
