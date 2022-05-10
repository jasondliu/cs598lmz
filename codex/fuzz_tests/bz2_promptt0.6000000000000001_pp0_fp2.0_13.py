import bz2
# Test BZ2Decompressor

# Read the compressed file
decompressor = bz2.BZ2Decompressor()
f = open('../data/sample.bz2','rb')
data = f.read()
f.close()

# Decompress the data
uncompressed_data = decompressor.decompress(data)

# Write the uncompressed data
f = open('../data/sample.out','wb')
f.write(uncompressed_data)
f.close()

# Print the first 100 bytes
print(uncompressed_data[:100])

# <script.py> output:
#     b'BZh91AY&SY.\xc9]L\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?\xe7\xff\xe00\x01\x99\xaa\x00\x00\x00\x00i\x03\x00\x02\x0c\n'
