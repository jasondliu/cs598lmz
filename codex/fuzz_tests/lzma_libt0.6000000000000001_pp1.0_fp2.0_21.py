import lzma
lzma.decompress(z)

# do it again
z = lzma.compress(b"Hello, world! " * 100000000)
lzma.decompress(z)
