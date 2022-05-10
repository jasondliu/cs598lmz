import lzma
# Test LZMADecompressor
assert lzma.LZMADecompressor().decompress(open('data/thomas.tar.xz', 'rb').read()) == open('data/thomas.tar', 'rb').read()

# Now the usual
import pickle
import io
import base64
import bz2

# Get bytes from file
with open('data/thomas.tar.xz', 'rb') as f:
    data = f.read()

# Decompress, decompress pickle, load
with lzma.LZMADecompressor() as lz:
    data = pickle.loads(lz.decompress(data))

# Save data
with open('data/output.jpg', 'wb') as f:
    f.write(data)
