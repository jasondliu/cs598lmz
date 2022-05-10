from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# The same as above
bz2.decompress(bz2_data)

# Compressing a file
# The compress() function takes a string
import bz2
uncompressed_data = b'We are the knights who say Ni!'
bz2_data = bz2.compress(uncompressed_data)

# The same as above
with open('knights.txt', 'wt') as f:
    f.write(uncompressed_data.decode('ascii'))

with open('knights.txt', 'rb') as f:
    data = f.read()

len(data)

with open('knights.bz2', 'wb') as f:
    f.write(bz2.compress(data))

with open('knights.bz2', 'rb') as f:
    data = f.read()

len(data)

# Compressing a file with a context manager
import bz2
with bz2.BZ2File('kn
