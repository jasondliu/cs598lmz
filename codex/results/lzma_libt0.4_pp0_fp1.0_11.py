import lzma
lzma.open('test.txt.lzma', 'r').read()

# Compression level
lzma.open('test.txt.lzma', 'r', preset=9).read()

# Check integrity
lzma.open('test.txt.lzma', 'r', check=lzma.CHECK_CRC64).read()

# Decompress
lzma.open('test.txt.lzma', 'r').read()

# Decompress
lzma.open('test.txt.lzma', 'r').read()

# Decompress
lzma.open('test.txt.lzma', 'r').read()

# Decompress
lzma.open('test.txt.lzma', 'r').read()

# Decompress
lzma.open('test.txt.lzma', 'r').read()

# Decompress
lzma.open('test.txt.lzma', 'r').read()

# Decompress
lzma.open('test.
