import lzma
# Test LZMADecompressor
with open('test.lzma', 'rb') as orig_file:
    with lzma.open(orig_file, 'rb') as decompressed:
        for line in decompressed:
            print(line)

# Test LZMACompressor
with open('test.lzma', 'wb') as compressed:
    with lzma.open(compressed, 'w') as comp:
        comp.write(b'abcdefghijklmnopqrstuvwxyz')

with open('test.lzma', 'rb') as orig_file:
    with lzma.open(orig_file, 'rb') as decompressed:
        print(decompressed.read())

# Test LZMAFile
with open('test.lzma', 'rb') as orig_file:
    with lzma.LZMAFile(orig_file) as decompressed:
        print(decompressed.read())

# Test LZMAFile with mode
