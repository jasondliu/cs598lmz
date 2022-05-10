import bz2
# Test BZ2Decompressor object

with open('example.json.bz2', 'rb') as source:
    decompressor = bz2.BZ2Decompressor()
    un_compressed_data = decompressor.decompress(source.read())
    print(un_compressed_data)

# Test BZ2Compressor object

with open('example.json', 'rb') as source:
    compressor = bz2.BZ2Compressor()
    compressed_data = b''.join(compressor.compress(source.read()) for i in range(9))
    compressed_data += compressor.flush()
    print(compressed_data)

# Using contextlib.closing()

with closing(bz2.BZ2File('example.json.bz2')) as uncompressed:
    text = uncompressed.read()

with bz2.BZ2File('example.json.bz2', 'w') as compressed:
    compressed.write(text)
