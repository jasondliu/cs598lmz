import bz2
bz2.decompress(d)

# q176 is open_files.in and q177 is open_files.out
with open('q176.in', 'rb') as f:
    header = f.read(1)
    d = f.read()
    with open('q176.out', 'wb') as f:
        f.write(d)

with open('q177.in', 'rb') as f:
    header = f.read(1)
    d = f.read()
    with open('q177.out', 'wb') as f:
        f.write(d)

# q177.out was edited to add zlib, gzip and bz2 headers
with open('q177.out', 'rb') as f:
    d = f.read()

zlib.decompress(d)
gzip.decompress(d)
bz2.decompress(d)

# lut.py
# Brute force all strings from length 6 to 7 to test for compression
lut = {}

def compress_test(s):
