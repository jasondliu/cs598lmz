from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Check if the file is gzip compressed
try:
    zfile = gzip.open(filename)
    data = zfile.read()
    zfile.close()
except IOError:
    print('Not gzipped.')

# Check if the file is bzip2 compressed
try:
    zfile = bz2.open(filename)
    data = zfile.read()
    zfile.close()
except IOError:
    print('Not bzip2ed.')

# Check if the file is lzma compressed
try:
    zfile = lzma.open(filename)
    data = zfile.read()
    zfile.close()
except IOError:
    print('Not lzmaed.')
