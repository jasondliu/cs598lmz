import lzma
# Test LZMADecompressor class
decomp = lzma.LZMADecompressor()

# Read xz file and decompress
with open('data/ex_lzma.xz', 'rb') as f_in:
    data = decomp.decompress(f_in.read())

# Print data
print(data)

# Close decompressor
decomp.close()

# Print data type
print(type(data))

# Print decompressor status
print(decomp.eof)


# Import bz2 module
import bz2

# Test BZ2Decompressor class
decomp = bz2.BZ2Decompressor()

# Read bz2 file and decompress
with open('data/ex_bz2.bz2', 'rb') as f_in:
    data = decomp.decompress(f_in.read())

# Print data
print(data)

# Close decompressor
decomp.close()

# Print data type
print(type(data))

# Print decompressor status
print(decomp.e
