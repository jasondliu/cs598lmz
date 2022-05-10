import bz2
bz2.BZ2File('/tmp/bz2file.bz2', 'wb').write(b'hello world')

bz2.BZ2File('/tmp/bz2file.bz2', 'rb').read()

# The bz2 module also includes a convenience function for decompressing files.
bz2.decompress(bz2.BZ2File('/tmp/bz2file.bz2', 'rb').read())

# The output from the bz2 module is compatible with the input of the zlib module.
import zlib

zlib.decompress(bz2.BZ2File('/tmp/bz2file.bz2', 'rb').read())

# bz2.open() works like the built-in open() but handles compressed files automatically.
with bz2.open('/tmp/bz2file.bz2', 'rt') as f:
    print(f.read())

# The bz2 module has a compression ratio similar to that of gzip but is slightly slower.
# It is not
