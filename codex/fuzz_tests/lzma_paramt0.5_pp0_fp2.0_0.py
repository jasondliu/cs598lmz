from lzma import LZMADecompressor
LZMADecompressor()

# now we can decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# and the original data is back
print(decompressed_data)
# b'hello world!hello world!hello world!hello world!'

# It also works with files
with open('lorem.txt', 'rb') as input, open('lorem_compressed.xz', 'wb') as output:
    compressor = LZMACompressor()
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(compressor.compress(block))
    output.write(compressor.flush())

# The compressed file is smaller than the original
import os
os.stat('lorem.txt').st_size
# 57909
os.stat('lorem_compressed.xz').st_size
# 21885

# and we can decompress it with the LZMADecompressor class
with open('lorem_compressed.xz', 'rb') as input, open('lorem_dec
