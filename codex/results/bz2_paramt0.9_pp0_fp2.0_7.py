from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(zz)
if zz[:4] != b'BZh':
    raise ValueError("generated with incorrect version of bzip2")
random_bytes = BZ2Decompressor().decompress(zz[4:])
assert(len(random_bytes) == 10000)
 
# You can generate random_bytes yourself if you want, but this is purposefully
# a non-trivial task as I don't expect you to be able to do it.
for i in range(10):
    print(random_bytes[i], end = ' ')
print()

a = 0
for idx, val in enumerate(random_bytes):
    a ^= val
    a <<= 1
    a %= 2 ** 64

with open('bzip.seed', 'wb') as f:
    f.write(struct.pack('<Q', a))
