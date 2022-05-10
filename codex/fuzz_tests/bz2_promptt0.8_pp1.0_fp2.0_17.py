import bz2
# Test BZ2Decompressor

# Setup buffer
buf = bz2.BZ2Decompressor()

# Some data to decompress
data = b"BZh91AY&SY\xd8\x00\x00\x00\x80\x00\x10\x00 \x00!\x9ah3M\x13<]\xc9\x14\xe1BA\x06\x00\x00\x00\x01"

# Decompress and print result
print(buf.decompress(data))

# Decompress and print result
print(buf.decompress(b""))
