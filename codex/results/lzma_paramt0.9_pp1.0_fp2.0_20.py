from lzma import LZMADecompressor
LZMADecompressor()

import os
import time

MAX_SIZE = 102400

compressed = b""

with open("flag.xz", 'rb') as f:
    while True:
        chunk = f.read(MAX_SIZE)
        if len(chunk) == 0:
            break
        compressed += chunk

uncompressed = LZMADecompressor().decompress(compressed)

with open('flag.txt', 'wb') as f:
    f.write(uncompressed)

os.remove('flag.xz')
