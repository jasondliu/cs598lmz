from lzma import LZMADecompressor
LZMADecompressor().decompress(x)

# compression using XZ
x = lzma.compress(b"Hello world!")
lzma.decompress(x)

# compressing and decompressing using bz2
bz2.compress(b"hello world!")
bz2.decompress(x)

# a context manager class
import bz2
with bz2.BZ2Compressor() as comp:
    with comp.compress(b"hello") as more:
        more(b"world!")

# if your data is already in a file, you can use a bz2.BZ2File to open it
# and compress or decompress the data inside
with bz2.BZ2File('datafile.bz2', 'wb') as f:
    f.write(b"Hello world!\n")

with bz2.BZ2File('datafile.bz2', 'rb') as f:
    print(f.read())
