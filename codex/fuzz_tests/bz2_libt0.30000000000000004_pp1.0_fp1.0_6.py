import bz2
bz2.BZ2File(filename, 'w')

# Writing to a compressed file
with bz2.BZ2File(filename, 'w') as f:
    f.write(bytes)

# Reading from a compressed file
with bz2.BZ2File(filename, 'r') as f:
    data = f.read()

# Compressing data at runtime
import bz2
uncompressed_data = b'Very long string goes here'
compressed_data = bz2.compress(uncompressed_data)

# Decompressing data at runtime
import bz2
compressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
uncompressed_data = bz2.decompress(compressed_data)

# Reading and writing
