from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# You can also provide a pre-allocated output buffer to decompress()
# to avoid memory allocations.
# This is most useful when decompressing multiple files back-to-back
# without gap to avoid reallocating the output buffer for each file.
output = bytearray()
with open('lorem.txt', 'rb') as input:
    decompressor = LZMADecompressor()
    while True:
        chunk = input.read(64 * 1024)
        if len(chunk) == 0:
            break
        output += decompressor.decompress(chunk, 64 * 1024)
    output += decompressor.flush()

output

# You can also decompress an entire file in one step using
# LZMADecompressor.decompressfile()
with open('lorem.txt.xz', 'rb') as input, \
     open('lorem.txt', 'wb') as output:
    LZMADecompressor().decompressfile(input, output)
