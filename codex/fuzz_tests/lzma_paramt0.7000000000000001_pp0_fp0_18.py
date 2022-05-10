from lzma import LZMADecompressor
LZMADecompressor()

# Create a compress object
comp = lzma.LZMACompressor()

# Wrap the compress object with an io.BufferedWriter
# to get an io.BufferedWriter object
f = io.BufferedWriter(comp, write_size=16384)

# Write data
f.write(b'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
f.write(b'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
f.write(b'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst
