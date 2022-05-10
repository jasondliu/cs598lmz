from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# use `xz` to compress the file
import subprocess
with open('lorem.txt', 'rb') as input, open('lorem.xz', 'wb') as output:
    compressor = subprocess.Popen(
        ['xz', '--compress'],
        stdin=input, stdout=output
    )
    compressor.wait()

# use `xz` to decompress the file
import os
with open('lorem.xz', 'rb') as input, open('lorem_from_xz.txt', 'wb') as output:
    decompressor = subprocess.Popen(
        ['xz', '--decompress'],
        stdin=input, stdout=output
    )
    decompressor.wait()

# use `bz2` to compress the file
with open('lorem.txt', 'rb') as input, open('lorem.bz2', 'wb') as output:
    compressor = subprocess.Popen(
        ['bzip2', '--compress'],
