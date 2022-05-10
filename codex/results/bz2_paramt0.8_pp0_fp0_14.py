from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# To compress you will need to use "bz2.compress"

import bz2
c = bz2.compress(b'hello')  # 5 bytes compressed to save space
print(c)
