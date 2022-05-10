import bz2
bz2.open(filename, mode='wt', compresslevel=9)
 
# Read/write compressed data.
# The opened file works like a regular Python file object, but data read is transparently decompressed and data written is transparently compressed:
with bz2.open(filename, mode='rt') as f:
    data = f.read()
print(data)
 
with bz2.open(filename, mode='wt') as f:
    f.write(data)
 
# Specifying a compresslevel=0 disables compression altogether, while values in the range 1-9 control the trade-off between speed and compression ratio (1 is fastest and produces the least compression, and 9 is slowest and produces the most compression). The default compresslevel is 9.
 
with gzip.open(filename, mode='wt', encoding='latin-1') as f:
    f.write(text)
 
import pathlib
p = pathlib.Path('example.bz2')
print(p.read_text(encoding='latin-1'))
 
# bz2 module documentation: https://
