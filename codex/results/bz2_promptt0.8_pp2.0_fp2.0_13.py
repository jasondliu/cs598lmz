import bz2
# Test BZ2Decompressor
decom = bz2.BZ2Decompressor()
decom.decompress(bz2.compress(b'hello world!'))

# Test decompress file
data = open('/home/feng/bz2_compress.dat', 'rb').read()
decom.decompress(data)

# BZ2Decompressor can be used as a context manager, resetting itself after exiting the context
with bz2.BZ2Decompressor() as f:
    data = f.read(100)

# bz2.BZ2File
# mode can be 'r' or 'w' or 'rb' or 'wb'
open('/home/feng/bz2_compress.dat', 'rb').read()
with bz2.BZ2File('/home/feng/bz2_compress.dat', 'wb') as f:
    f.write(b'hello world!')

with bz2.BZ2File('/home/feng/bz2_compress.dat', 'rb')
