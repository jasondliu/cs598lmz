import bz2
bz2.decompress(data)

# bz2.decompress(data)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.6/bz2.py", line 226, in decompress
#     return self._decompressor.decompress(data)
#   File "/usr/lib/python3.6/bz2.py", line 431, in decompress
#     raise BZ2Decompressor.error("BZ2 data stream does not start with a magic byte")
# bz2.BZ2Decompressor.error: BZ2 data stream does not start with a magic byte

# bz2.decompress(data[1:])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.6/bz2.py", line 226, in decompress
#     return self._decompressor.decompress(data)
#  
