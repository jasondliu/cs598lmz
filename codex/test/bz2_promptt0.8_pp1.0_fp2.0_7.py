import bz2
# Test BZ2Decompressor.readinto()

decompressor = bz2.BZ2Decompressor()

# This is an array of 10 bytes. 8 of those bytes are the same, meaning that the
# compressor will likely not be able to produce a shorter compressed output.
# Two bytes will be different and will likely be shorter.
unused_buf = bytearray(b'12345678ab')

# Compress data so that it will produce some unique bytes.
cmp_buf = bz2.compress(unused_buf)

# First test the case where all the bytes in the original buffer, unused_buf,
# are consumed.
decompressor.decompress(cmp_buf, max_length=8)

# Read it back into unused_buf.
