import bz2
# Test BZ2Decompressor
file = bz2.BZ2File('data/sample.csv.bz2', 'r')
print file.read(50)

decom = bz2.BZ2Decompressor()

decom_file = open('data/sample.csv', 'r')
text = file.read(50)

while text:
    text = decom.decompress(text)
    print text
    text = file.read(50)

decom_file.close()

# Test BZ2 compressor
compressed_file = bz2.BZ2File('data/sample_compressed.csv.bz2', 'w')
uncompressed_file = open('data/sample.csv', 'r')
compressor = bz2.BZ2Compressor()
data = uncompressed_file.read(50)
compressed_file.write(compressor.compress(data))

while data:
    data = uncompressed_file.read(50)
    compressed_file.write(compressor.compress(data))

compressed_file.
