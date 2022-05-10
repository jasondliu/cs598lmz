import lzma
# Test LZMADecompressor object
compressor = lzma.LZMADecompressor()
print(compressor)
for string in ['abcd', 'abcdb', 'abcdbd']:
    print(string, compressor.decompress(compressor.compress(string)))
buffer = bytearray(b'Hello world!')
print(buffer)
print(compressor.decompress(compressor.compress(buffer)))
print(buffer)
with open('lorem.txt', 'rb') as input, \
     lzma.open('lorem-compress.xz', 'wt') as output:
    output.write(input.read())

with lzma.open('lorem-compress.xz', 'rt') as compressed:
    original_text = compressed.read()
original_text
 
with lzma.open('lorem-compress.xz') as compressed:
    binary_data = compressed.read()
binary_data

# construct LZMACompressor w/ mf=1 & lc=4 to mimic XZ w/ --extreme
comp
