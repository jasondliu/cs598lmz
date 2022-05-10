import bz2
bz2.decompress(data)

# Compression
data = open('file.txt', 'rb').read()
len(data)

compressed = bz2.compress(data)
len(compressed)

bz2.decompress(compressed)

# Compress into a file
f = bz2.open('file.bz2', 'wt')
f.write('Contents of the example file go here.\n')
f.close()

f = bz2.open('file.bz2', 'rt')
f.read()
f.close()

# Compress a file with a specified compression level
import bz2

uncompressed_data = b'Very similar to a file. It contains a sequence of bytes that can be stored or transmitted.\n'
print('UNCOMPRESSED: {} bytes'.format(len(uncompressed_data)))

for i in range(1, 10):
    filename = 'file_compress_level_{}.bz2'.format(i)
    with bz2.open(filename, 'wt
