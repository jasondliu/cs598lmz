from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# source: https://docs.python.org/3.8/library/bz2.html
# example 2 (output the compressed data to a text file, then extract it back to another file)
import bz2
to_read = b"this is a fi"
to_write = b"good.txt"
f = open(to_write, "wb")
f.write(bz2.compress(to_read))
f.close()
f = bz2.BZ2File(to_write)
data = f.read()
print(data)

to_write = b"another_good.txt"
f = open(to_write, "wb")
f.write(data)
f.close()

# source: https://docs.python.org/3.8/library/bz2.html
# example 3 (write compressed data to a file-like object)
import sys
import bz2
uncompressed_data = b'We are not pleased!  See Spot run.  Run, Spot.  Run!'
comp
