import bz2
bz2.decompress(bz2.compress(b'Hello world!'))

# bz2.open accepts either a string or a file handle
with bz2.open('test.bz2', 'w') as f:
    f.write(b"Hello world!")

# bz2.open accepts either a string or a file handle
with bz2.open('test.bz2', 'r') as f:
    contents = f.read()
contents

# BZ2File.fileno() returns the underlying file descriptor.
# This means you can use bz2file.fileno() with select.select().
import select
rlist, wlist, xlist = select.select([bz2.BZ2File('test.bz2')], [], [])

# Use bz2.BZ2File in a context manager and it will close automatically
with bz2.BZ2File('test.bz2') as f:
    f.write(b"Hello world!")

# BZ2Compressor and BZ2Decompressor
