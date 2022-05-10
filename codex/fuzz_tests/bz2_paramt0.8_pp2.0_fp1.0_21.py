from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bytes(bz2data))

# 2
print(len(bz2data))

# 3
import bz2
bz2.decompress(bz2data)

# 4
import bz2
bz2.decompress(bytes(bz2data))

# 5
bz2data.decode()

# 6
bz2data.decode('utf-8')

# 7
bz2data.decode('latin1')

# 8
import bz2
len(bz2.decompress(bz2data))

# 9
bz2.decompress(bz2data).decode()

# 10
bz2data.decompress()

# 11
bz2data.decompress()

# 12
bytes(bz2data).decompress()

# 13
bz2data.decode().decompress()

# 14
bz2data.decompress().decode()

# 15
bz2data.en
