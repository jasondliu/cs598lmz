import bz2
bz2.decompress(compressed)

# Compress a file
import bz2
uncompressed = b'We are the knights who say Ni!'
with open('uncompressed.txt', 'wb') as f:
    f.write(uncompressed)
with open('uncompressed.txt', 'rb') as f:
    compressed = bz2.compress(f.read())
with open('compressed.bz2', 'wb') as f:
    f.write(compressed)

# Decompress a file
import bz2
with open('compressed.bz2', 'rb') as f:
    compressed = f.read()
with open('uncompressed.txt', 'wb') as f:
    f.write(bz2.decompress(compressed))
