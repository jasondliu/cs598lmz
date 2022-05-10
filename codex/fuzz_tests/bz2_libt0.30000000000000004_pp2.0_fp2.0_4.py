import bz2
bz2.decompress(data)

# bz2.decompress(data)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.5/bz2.py", line 232, in decompress
#     return self._decompressor.decompress(data)
#   File "/usr/lib/python3.5/bz2.py", line 442, in decompress
#     raise BZ2Decompressor.error("Not enough data for a block")
# bz2.BZ2Decompressor.error: Not enough data for a block

# bz2.decompress(data)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.5/bz2.py", line 232, in decompress
#     return self._decompressor.decompress(data)
#   File "/usr/lib/python3.5/bz2.
