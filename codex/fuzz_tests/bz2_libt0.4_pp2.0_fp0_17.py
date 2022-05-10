import bz2
bz2.BZ2File

# Compress a file
with bz2.BZ2File('compressed.bz2', 'w') as f:
    f.write(b'This is a test')

# Read a compressed file
with bz2.BZ2File('compressed.bz2', 'r') as f:
    print(f.read())

# Compress a file using a compression level
with bz2.BZ2File('compressed.bz2', 'w', compresslevel=9) as f:
    f.write(b'This is a test')

# Compress a file using a compression level
with bz2.BZ2File('compressed.bz2', 'w', compresslevel=9) as f:
    f.write(b'This is a test')

# Compress a file using a compression level
with bz2.BZ2File('compressed.bz2', 'w', compresslevel=9) as f:
    f.write(b'This is a test')

# Compress a file using
