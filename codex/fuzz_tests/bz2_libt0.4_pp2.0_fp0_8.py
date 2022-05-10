import bz2
bz2.decompress(compressed)

# bz2.decompress(compressed)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/bz2.py", line 225, in decompress
#     return BZ2Decompressor().decompress(data)
#   File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/bz2.py", line 572, in decompress
#     self._stream.close()
#   File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/bz2.py", line 758, in close
#     raise BZ2Decompressor.error(self.decompress_errno)
# bz2
