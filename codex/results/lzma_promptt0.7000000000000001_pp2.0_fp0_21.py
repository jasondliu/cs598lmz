import lzma
# Test LZMADecompressor.

# Note that the LZMA module only exists in Python 2.7; it does not exist in
# Python 3.2.

# A large file with known data.
# The file was created by
#   cat /dev/urandom | head -c 104857600 > /tmp/random
# and then compressed with
#   xz --stdout /tmp/random > /tmp/random.xz

# Read compressed data.
compressed = open("/tmp/random.xz", "rb").read()

# Create decompressor.
decomp = lzma.LZMADecompressor()

# Decompress.
decompressed = decomp.decompress(compressed)

# Compare with original.
original = open("/tmp/random", "rb").read()
count = 0
for decomp_c, orig_c in zip(decompressed, original):
    if decomp_c != orig_c:
        print("Error at %d: %d != %d" % (count, decomp_c, orig_c))
        break
    count += 1
