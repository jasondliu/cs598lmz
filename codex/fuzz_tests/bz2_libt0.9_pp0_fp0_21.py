import bz2
bz2.decompress(b)

# bz2.decompress(a)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.4/bz2.py", line 206, in decompress
#     return self._decompressor.decompress(data, size)
#   File "/usr/lib/python3.4/bz2.py", line 436, in decompress
#     raise BZ2DecompressError("Decompressor is used twice")
# bz2.BZ2DecompressError: Decompressor is used twice

d = bz2.BZ2Decompressor()
d.decompress(a)
d.decompress(b)

d.decompress(a)
d.decompress(b)

d.decompress(b'BZh91AY&SY')

d = bz2.BZ2Decompressor()
d.decompress(a)
d.decompress
