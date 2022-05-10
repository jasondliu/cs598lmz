import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xff\xff\xff\x01\x00?'
bzd = bz2.BZ2Decompressor()
bzd.decompress(data)
bzd.flush()

# Read in a small file
f = open("./data/cars93.csv", "rb")
bzdata = f.read()
f.close()

# Decompress the data and print it out
bz_d = bz2.BZ2Decompressor()
print(bz_d.decompress(bzdata))

# Compress the file
f = open("./data/cars93.csv", "rb")
bzdata = bz2.compress(f.read())

# Decompress the file
print(bz2.decompress(bzdata))

# Another example of compressing a file in binary mode
import os
os.
