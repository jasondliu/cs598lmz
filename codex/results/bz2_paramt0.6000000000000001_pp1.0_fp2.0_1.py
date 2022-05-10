from bz2 import BZ2Decompressor
BZ2Decompressor().decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Install module
# python -m pip install bz2
# or
# python -m pip install --user bz2

# Import module
import bz2

# Decompress data
un = bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Print decompressed data
print(un)

# Print password
print(un.decode("utf-8"))
