import lzma
# Test LZMADecompressor object

ctext = lzma.compress(b'The quick brown fox jumps over the lazy dog.')

print(ctext)

d = lzma.LZMADecompressor()
d.decompress(ctext)

print(d.unused_data)
print(d.eof)

# Decompress a file

with lzma.open('foo.xz', 'rb') as f:
    file_content = f.read()

print(file_content)

# You can also use the LZMAFile class directly:

with lzma.LZMAFile('foo.xz') as f:
    file_content = f.read()

print(file_content)

# Compress a file

with lzma.open('foo.xz', 'w') as f:
    f.write(b"Hello, world!\n")

# You can also use the LZMAFile class directly:

with lzma.LZMAFile('foo.xz', mode='w') as
