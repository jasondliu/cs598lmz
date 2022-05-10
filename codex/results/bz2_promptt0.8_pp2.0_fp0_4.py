import bz2
# Test BZ2Decompressor
data = open(filename, "rb").read()
compressor = bz2.BZ2Compressor()
cb = compressor.compress(data)
cb += compressor.flush()
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(cb).decode('utf-8'))
# Test BZ2File
with bz2.BZ2File(filename+'.bz2', 'w') as f:
    f.write(data)
with bz2.BZ2File(filename+'.bz2', 'r') as f:
    print(f.read().decode('utf-8'))
'''

# zlib module
'''
# The zlib module provides a lower-level interface to many of the functions in the zlib compression library from the GNU project.

import zlib
# Test Compress
s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.dec
