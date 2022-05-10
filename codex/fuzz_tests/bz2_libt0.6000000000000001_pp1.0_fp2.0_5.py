import bz2
bz2.decompress(bz2_compressed)

# Compression in Python
import bz2
original_data = b"This is the original text."
print('Original: {} bytes'.format(len(original_data)))
compressed = bz2.compress(original_data)
print('Compressed: {} bytes'.format(len(compressed)))
decompressed = bz2.decompress(compressed)
print('Decompressed: {}'.format(decompressed))

# Compression with gzip
import gzip
original_data = b"This is the original text."
with gzip.open('my_compressed_file.gz', 'wb') as f:
    f.write(original_data)

with gzip.open('my_compressed_file.gz', 'rb') as f:
    print(f.read())

# Compression with gzip
import gzip
with gzip.open('my_compressed_file.gz', 'rb') as input, \
        open('decompressed_file.txt', 'wb') as output
