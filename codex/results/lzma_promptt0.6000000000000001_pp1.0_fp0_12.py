import lzma
# Test LZMADecompressor

# Writing to a file
with open('sample.xz', 'rb') as f_in, lzma.open('sample.txt', 'wt') as f_out:
    f_out.write(f_in.read())
    
# Reading directly
with lzma.open('sample.xz') as f_in:
    print(f_in.read())

# Reading directly
with lzma.open('sample.xz') as f_in:
    print(f_in.read(10))
    print(f_in.read(10))
    print(f_in.read(10))

# Reading and writing directly
with lzma.open('sample.xz') as f_in, open('sample.txt', 'wt') as f_out:
    f_out.write(f_in.read())

# Reading and writing directly
with lzma.open('sample.xz', 'rt') as f_in, open('sample.txt', 'wt') as f_out:
    f_out.write(f_in.
