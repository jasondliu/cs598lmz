from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# uncompress data
with open(compressed_file, 'rb') as infile:
    data = infile.read()
with open(uncompressed_file, 'wb') as outfile:
    outfile.write(BZ2Decompressor().decompress(data))

# compress data
with open(uncompressed_file, 'rb') as infile:
    data = infile.read()
with open(compressed_file, 'wb') as outfile:
    outfile.write(BZ2Compressor().compress(data))
