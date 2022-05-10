import lzma
# Test LZMADecompressor

# Compress a file
with open('lorem.txt', 'rb') as f_in, lzma.open('lorem.xz', 'wb') as f_out:
    f_out.write(f_in.read())

# Decompress a file
with lzma.open('lorem.xz') as f_in, open('lorem_copy.txt', 'wb') as f_out:
    f_out.write(f_in.read())
# Test LZMADecompressor

# Compress a file
with open('lorem.txt', 'rb') as f_in, lzma.open('lorem.xz', 'wb') as f_out:
    f_out.write(f_in.read())

# Decompress a file
with lzma.open('lorem.xz') as f_in, open('lorem_copy.txt', 'wb') as f_out:
    f_out.write(f_in.read())
# Test LZMADecompressor

# Comp
